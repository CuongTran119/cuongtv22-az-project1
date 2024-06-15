# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

_For **both** a VM or App Service solution for the CMS app:_

- _Analyze costs, scalability, availability, and workflow_

  - Cost: VMs can be cost-effective for certain workloads, but App Services can be more cost-effective for smaller applications.
  - Availability: VMs need to configuration for high availability., while App Services provides built-in load balancing and auto-scaling features..
  - Scalability: App Services are easier to scale as they handle infrastructure for you, whereas VMs require manual scaling.
  - Complexity: VMs are more suitable for complex applications with specific requirements, while App Services are simpler and ideal for common use cases.
  - Workflow: VMs provides a fully cotrol for OS, network, and application while App Services has limited control over underlying infrastructure, focused on application deployment.

- I see that App Service is more appropriate for deploy CMS app than VM because:
  - The availability and redundancy of App Service is very high.
  - App Service simplify deployment and scaling.
  - App Service support to run CI/CD quicky and easily.
  - Beside that the CMS app is not too big, using App Service can be cost-effective as they reduce infrastructure management overhead.

### Assess app changes that would change your decision.

    - I will change my decision in case changing app from an on-premises environment to the Cloud.
    - When I need custom configurations, including non-standard software or extensive networking setup.
    - Also I am in case handling Resource-Intensive Workloads such as: running complex databases or high-performance computing.
