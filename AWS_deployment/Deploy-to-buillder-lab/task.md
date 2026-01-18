
### Learning objectives

By completing this task, you will be able to:
- **Deploy containerized applications to AWS ECS** - Experience deploying multi-service Flask applications to a production-ready container orchestration platform.
- **Configure AWS infrastructure** - Set up and work with AWS services including ECS, ECR, ALB, and EC2 instances in a hands-on lab environment.
- **Implement container registry workflows** - Push Docker images to Amazon ECR and configure ECS to pull images from the registry.
- **Understand microservices deployment patterns** - Deploy the complete inventory management system with gateway and API services as separate containers.

### Problem context

Deploying containerized microservices to production requires understanding both container orchestration and cloud infrastructure. This task bridges the gap between local Docker development and production-ready AWS deployments.

**Why this deployment approach matters:**
- **Real-world scalability**: ECS provides auto-scaling, health checks, and load balancing for production workloads.
- **Industry standard practices**: Learn the same deployment patterns used by companies running microservices at scale.
- **Complete DevOps pipeline**: Experience the full cycle from code to production deployment.

**What makes this challenging:**
- **Infrastructure complexity**: Managing multiple AWS services that must work together.
- **Container orchestration**: Understanding how ECS schedules and manages containers across multiple hosts.
- **Network configuration**: Setting up proper communication between services and load balancing.

## Implementation requirements

Deploy your complete Flask microservices application (gateway + inventory system) to AWS using Elastic Container Service (ECS). 

You can practice with Elastic Container Service for free using the [AWS Free Tier](https://aws.amazon.com/free/).

Please follow the instructions in these guides:
 - [Building and Deploying Containers Using Amazon Elastic Container Service](https://github.com/jetbrains-academy/skillpath-aws-freetier-labs-instruction/blob/main/Building%20and%20Deploying%20Containers%20Using%20Amazon%20Elastic%20Container%20Service.md)
 - [Working with Amazon Elastic Container Service](https://github.com/jetbrains-academy/skillpath-aws-freetier-labs-instruction/blob/main/Working%20with%20Amazon%20Elastic%20Container%20Service.md)