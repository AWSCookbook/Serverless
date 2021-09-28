from constructs import Construct
from aws_cdk import (
    aws_ec2 as ec2,
    aws_elasticloadbalancingv2 as alb,
    Stack,
    CfnOutput,
)


class CdkAwsCookbook501Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        public_subnets = ec2.SubnetConfiguration(
            name="PUBLIC",
            subnet_type=ec2.SubnetType.PUBLIC,
            cidr_mask=24
        )

        # create VPC
        vpc = ec2.Vpc(
            self,
            'AWS-Cookbook-VPC-501',
            cidr='10.10.0.0/23',
            subnet_configuration=[public_subnets]
        )

        albSecurityGroup = ec2.SecurityGroup(
            self,
            'albSecurityGroup',
            vpc=vpc,
            allow_all_outbound=True,
            description='Security Group for the ALB',
        )

        albSecurityGroup.add_ingress_rule(
            peer=ec2.Peer.ipv4("0.0.0.0/0"),
            connection=ec2.Port.tcp(80),
            description='Allow HTTP from the world',
            remote_rule=False
        )

        LoadBalacner = alb.ApplicationLoadBalancer(
            self,
            'LoadBalacner',
            vpc=vpc,
            internet_facing=True,
            security_group=albSecurityGroup,
            vpc_subnets=ec2.SubnetSelection(
                one_per_az=False,
                subnet_type=ec2.SubnetType('PUBLIC')
            )
        )

        Listener = alb.ApplicationListener(
            self,
            'listener80',
            load_balancer=LoadBalacner,
            open=False,
            port=80,
            protocol=alb.ApplicationProtocol('HTTP')
        )

        Listener.add_action(
            'Fixed',
            action=alb.ListenerAction.fixed_response(
                status_code=200,
                message_body="AWS Cookbook Fixed Content for ALB"
            )
        )

        # outputs
        CfnOutput(
            self, 'LoadBalancerDns',
            value=LoadBalacner.load_balancer_dns_name
        )

        CfnOutput(
            self,
            'ListenerArn',
            value=Listener.listener_arn
        )

        CfnOutput(
            self,
            'VpcId',
            value=vpc.vpc_id
        )

        CfnOutput(
            self,
            'AlbArn',
            value=LoadBalacner.load_balancer_arn
        )

        public_subnets = vpc.select_subnets(subnet_type=ec2.SubnetType.PUBLIC)

        CfnOutput(
            self,
            'PublicSubnets',
            value=', '.join(map(str, public_subnets.subnet_ids))
        )
