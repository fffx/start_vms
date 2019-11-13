# -*- coding: utf-8 -*-

from wox import Wox
import os
from os.path import expanduser
class VmManager(Wox):

    def query(self, query):
        vm_home = expanduser("~/VirtualBox VMs")
        results = []
        if !os.path.isdir(vm_home)
            return results

        # results.append({
        #     "Title": "Hello World",
        #     "SubTitle": "Query: {}".format(query),
        #     "IcoPath":"Images/app.ico",
        #     "ContextData": "ctxData"
        # })

        vm_names = os.listdir(vm_home)
        for vm_name in vm_names:
            if query in vm_name:
                results.append({
                    "Title": vm_name,
                    "IcoPath":"Images/app.ico",
                    "JsonRPCAction":{
                        "method": "start_vm",
                        "dontHideAfterAction":False
                    }
                })  
        return results

    def start_vm(self, data):
        cmd = "C:\\Program Files\\Oracle\\VirtualBox\\VBoxManage.exe\" startvm \"{}\" --type headless"
        os.system(cmd.format(data["Title"]))
        

if __name__ == "__main__":
    VmManager()