from aws_cdk import (
    core,
    aws_ecs as ecs,
    aws_ec2 as ec2
)

class CicdVpcEcsStack(core.Stack):
    def __init__(self, scope, id, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        vpc_nonprod = ec2.Vpc(self, "cicd-vpc-nonprod-laravel-api", max_azs=2)
        vpc_prod = ec2.Vpc(self, "cicd-prod-laravel-api", max_azs=2)

        ecs.Cluster(self, "cicd-ecs-nonprod-laravel-api", capacity_providers=["FARGATE"],cluster_name="cicd-ecs-nonprod-laravel-api",vpc=vpc_nonprod)
        ecs.Cluster(self, "cicd-ecs-prod-laravel-api", capacity_providers=["FARGATE"],cluster_name="cicd-ecs-prod-laravel-api",vpc=vpc_prod)
      


