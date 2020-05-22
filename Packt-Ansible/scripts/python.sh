#!/bin/bash
sudo apt-get update
sudo apt-get install -y python


{
  "appId": "88dde00e-e9f2-4327-937b-d1b2befac79a",
  "displayName": "azure-cli-2020-05-03-19-17-44",
  "name": "http://azure-cli-2020-05-03-19-17-44",
  "password": "b88683e8-46bd-439e-ac92-44b673135f80",
  "tenant": "e22aea6d-0cf8-4803-8e12-edaecd4fa3f2"
}


Packer:

manpreet@Azure:~$ az ad sp create-for-rbac --name $name --role="Contributor" --scopes="/subscriptions/$subId" --output json
Creating a role assignment under the scope of "/subscriptions/22e2b6ca-9ce9-4eb2-9cfd-01a2d500e1f5"
  Retrying role assignment creation: 1/36
{
  "appId": "a541049c-1d0f-4eb8-943c-3fe9925970d4",
  "displayName": "hashicorp",
  "name": "http://hashicorp",
  "password": "d722b3c5-fc11-4f32-a537-add9a09bdc8c",
  "tenant": "e22aea6d-0cf8-4803-8e12-edaecd4fa3f2"
}