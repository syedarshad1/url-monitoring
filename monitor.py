
import requests
from datetime import datetime


def monitor_url(url):
    report = {
        'URL': url,
        'Start Time': None,
        'End Time': None,
        'Total Time Taken': None,
        'HTTP Status Code': None,
        'Status': None,
        'Failure Reason': None
    }

    start_time = datetime.now()
    report['Start Time'] = start_time.isoformat()

    try:
        response = requests.get(url)
        end_time = datetime.now()
        report['End Time'] = end_time.isoformat()
        report['Total Time Taken'] = (end_time - start_time).total_seconds()
        report['HTTP Status Code'] = response.status_code
        report['Status'] = 'Success' if response.status_code == 200 else 'Failure'
        if response.status_code != 200:
            report['Failure Reason'] = f'HTTP Status Code: {response.status_code}'
    except Exception as e:
        end_time = datetime.now()
        report['End Time'] = end_time.isoformat()
        report['Total Time Taken'] = (end_time - start_time).total_seconds()
        report['Status'] = 'Failure'
        report['Failure Reason'] = str(e)

    with open('url_monitoring_report.md', 'w') as f:
        f.write(f"""## URL Monitoring Report

- **URL:** {report['URL']}
- **Start Time:** {report['Start Time']}
- **End Time:** {report['End Time']}
- **Total Time Taken:** {report['Total Time Taken']} seconds
- **HTTP Status Code:** {report['HTTP Status Code']}
- **Status:** {report['Status']}
- **Failure Reason:** {report['Failure Reason'] if report['Failure Reason'] else 'N/A'}
""")

monitor_url('https://api-gw1-prod1.fisglobal.com/gw/v1/health')
