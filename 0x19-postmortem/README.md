Postmortem: Web Stack Outage

Issue Summary:
Duration: January 15, 2024, 14:00 UTC to January 15, 2024, 16:30 UTC
Impact: Users experienced slow page loads and frequent 500 errors on our e-commerce platform. Approximately 75% of users were affected, leading to significant user frustration and potential loss of sales.
Root Cause: The root cause was a misconfiguration in the Nginx server settings, which led to a bottleneck during peak traffic.

Timeline:
14:00 UTC: Issue detected by automated monitoring system which alerted high error rates and slow response times.
14:05 UTC: On-call engineer receives the alert and starts investigating.
14:15 UTC: Initial investigation points to database overload; database team is notified.
14:30 UTC: Database team reports normal operation; focus shifts to application servers.
14:45 UTC: Web server logs show numerous 500 errors related to Nginx.
15:00 UTC: Network team examines Nginx configuration.
15:15 UTC: Misleading path: Suspected a recent code deployment caused the issue, but rollback showed no improvement.
15:30 UTC: Realization that a recent change in Nginx configuration had inadvertently limited available worker processes.
15:45 UTC: Nginx configuration corrected and servers restarted.
16:00 UTC: Monitoring shows gradual improvement.
16:30 UTC: All services confirmed operational and issue resolved.

Root Cause and Resolution:

Root Cause:
The outage was caused by a misconfiguration in the Nginx server settings. Specifically, a configuration file was updated incorrectly during routine maintenance. The number of worker processes was set too low, which couldn't handle the increased traffic during peak hours. This led to a bottleneck, causing slow response times and server errors.

Resolution:
The Nginx configuration was corrected by increasing the number of worker processes to match the server's capacity. The following steps were taken:

Identified the incorrect setting in the Nginx configuration file.
Increased the worker_processes directive to a value appropriate for the server's CPU count.
Restarted the Nginx service to apply the new configuration.
Monitored the server performance to ensure the issue was resolved.
Corrective and Preventative Measures

Improvements:
To prevent similar issues in the future, we need to enhance our configuration management and monitoring processes.

Tasks:

Implement Configuration Management:
Utilize a configuration management tool (e.g., Ansible, Chef) to manage and apply server configurations consistently.
Enhanced Monitoring:
Add monitoring for Nginx worker processes and other critical server parameters to catch configuration issues early.
Configuration Review:
Implement a mandatory peer-review process for all configuration changes to ensure accuracy and adherence to best practices.
Load Testing:
Regularly perform load testing to identify potential bottlenecks and ensure the system can handle peak traffic.
Training:
Conduct training sessions for the engineering team on best practices for server configuration and performance tuning.
Automated Alerts:
Set up automated alerts for when configurations deviate from the expected values.
By addressing these areas, we aim to reduce the likelihood of future outages and ensure a more robust and reliable system for our users.
