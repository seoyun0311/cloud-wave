import boto3
import time
import psutil
import pandas as pd
import streamlit as st

from widget.side_bar import start_process

class Homepage:
    def __init__(self):
        self.homepage()

    def get_instance_name_tag(self, ec2_client, instance_id):
        response = ec2_client.describe_instances(InstanceIds=[instance_id])
        
        for reservation in response["Reservations"]:
            for instance in reservation["Instances"]:
                # 태그 목록 내에서 'Name' 키를 가진 태그를 찾습니다.
                name_tag = next((tag['Value'] for tag in instance.get('Tags', []) if tag['Key'] == 'Name'), None)
                if name_tag:
                    return name_tag  # 'Name' 태그 값 반환
        return None
    
    def server_monitoring(self):
        # 상태 표시할 빈 컨테이너 생성
        col1, col2, col3, col4, col5, col6, col7= st.columns(7)

        cpu_slot = col1.empty()
        memory_slot = col2.empty()
        disk_usage_slot = col3.empty()
        uptime_slot = col4.empty()
        load_avg_slot_1 = col5.empty()
        load_avg_slot_5 = col6.empty()
        load_avg_slot_15 = col7.empty()

        while True:
            # 메트릭 정보 수집
            cpu_percent = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            disk_usage = psutil.disk_usage('/')
            load_average = psutil.getloadavg()
            uptime_seconds = time.time() - psutil.boot_time()

            # 컬럼에 메트릭 정보 표시
            cpu_slot.metric(label="CPU Usage", value=cpu_percent)
            memory_slot.metric(label="Memory Usage", value=memory.percent)
            disk_usage_slot.metric(label="Disk Usage", value=disk_usage.percent)

            uptime_info = f"{uptime_seconds / 60:,.0f} M"
            uptime_slot.metric(label="Uptime", value=uptime_info)

            load_avg_slot_1.metric(label="Load Avg(1)", value=f"{load_average[0]:.2f}")
            load_avg_slot_5.metric(label="Load Avg(5)", value=f"{load_average[1]:.2f}")
            load_avg_slot_15.metric(label="Load Avg(15)", value=f"{load_average[2]:.2f}")
            time.sleep(1)

    def homepage(self):
        st.title("AWS EC2 Information")
        col1, col2, col3 = st.columns([1, 1, 8])
        with col1:
            st.markdown("<span style='font-size: 15px; text-align: center;'>Start Monitoring</span>", unsafe_allow_html=True)
            placeholder_button = st.empty()
        with col2:
            st.markdown("<span style='font-size: 15px; text-align: center;'>Start Stress Test</span>", unsafe_allow_html=True)
            placeholder_stress = st.empty()
        with col3:
            placeholder_monitoring = st.empty()
        st.header('EC2 Instance Information Table', divider = "gray")

        with st.sidebar:
            st.sidebar.header('System Control Panner')
            timeout = st.sidebar.number_input('Enter timeout for the stress test:', value=300)

        # Local Labtop Version
        # EC2 Instance Information
        ec2_client = boto3.client('ec2')
        instance_id = 'i-0c63683edc7e9e389'
        name_tag = self.get_instance_name_tag(ec2_client, instance_id)
        ec2 = ec2_client.describe_instances(InstanceIds=[instance_id])
        for reservation in ec2['Reservations']:
            for instance in reservation['Instances']:
                ec2_metadata_info = {
                    "Name": name_tag,
                    "Instance ID": instance['InstanceId'],
                    "Instance Type": instance['InstanceType'],
                    "Private IP": instance['PrivateIpAddress'],
                    "Public IP": instance.get('PublicIpAddress', 'N/A'),
                    "Region": instance['Placement']['AvailabilityZone'][:-1],
                    "Availability Zone": instance['Placement']['AvailabilityZone'],
                }
        # EBS Volume Information
        volumes = ec2_client.describe_volumes(Filters=[{'Name': 'attachment.instance-id', 'Values': [instance_id]}])
        volume_data = []
        for volume in volumes['Volumes']:
            # volume_metadata_info = {}
            volume_data.append({
                'Instance ID': instance_id,
                'Volume ID': volume['VolumeId'],
                'Type': volume['VolumeType'],
                'Size (GB)': volume['Size'],
                'State': volume['State'],
                'Snapshot ID': volume.get('SnapshotId', 'N/A'),
                'IOPS': volume.get('Iops', 'N/A'),
                'Encrypted': volume['Encrypted'],
                'Creation Date': volume['CreateTime'].strftime('%Y-%m-%d %H:%M:%S')
            })

        # 데이터프레임 생성
        df_ec2 = pd.DataFrame(list(ec2_metadata_info.items()), columns=['Metadata', 'Value'])
        st.table(df_ec2)
        

        st.header('Storage Information Table', divider = "gray")
        # df_volume = pd.DataFrame(list(volume_metadata_info.items()),columns=['Metadata', 'Value_(1)', 'Value_(2)'])
        # st.table(df_volume)
        st.table(volume_data)
           
        with placeholder_button.container():
            if st.button("Push Button", use_container_width=True):
                with placeholder_stress.container():
                    if st.button("Stress Tool", use_container_width=True):
                        start_process(timeout)
                with placeholder_monitoring: self.server_monitoring()


        with placeholder_stress.container():
            if st.button("Stress Tool", use_container_width=True):
                start_process(timeout)
                with placeholder_monitoring: self.server_monitoring()