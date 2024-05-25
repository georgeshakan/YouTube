#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { CicdPipelineStack } from '../lib/cicd_pipeline-stack';

const app = new cdk.App();
new CicdPipelineStack(app, 'CicdPipelineStack', {
  env :{
    account: "891377007415",
    region: "us-east-1"
  },
  terminationProtection: false
});