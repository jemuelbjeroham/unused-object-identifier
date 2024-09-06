from panos import panorama
from panos import policies
from panos import objects 
import getpass
import csv

def check_in_shared_AGs(object_name, username, password):
    pano = panorama.Panorama(hostname="10.60.198.122", api_username=username, api_password=password)
    shared_AGs = objects.AddressGroup.refreshall(pano)
    count = 0
    for shared_AG in shared_AGs:
        if object_name in shared_AG.static_value and len(shared_AG.static_value) == 1:
            count = count + 1
            # check_in_shared_AGs(shared_AG.name, username, password)
            # check_in_AGs(shared_AG.name, username, password)
            # check_in_SRs(shared_AG.name, username, password)
            # check_in_shared_SRs(shared_AG.name, username, password)
        elif object_name in shared_AG.static_value:
            count = count + 1
            # shared_AG.static_value.remove(object_name)
            # shared_AG.apply()
            # print(f"removed {object_name} from Address Group {shared_AG.name} in shared scope")
            # if shared_AG.static_value == []:
            #     check_in_shared_AGs(shared_AG.name, username, password)
            #     check_in_AGs(shared_AG.name, username, password)
            #     check_in_SRs(shared_AG.name, username, password)
            #     check_in_shared_SRs(shared_AG.name, username, password)
            # else:
            #     continue
        else:
            continue
    return count

def check_in_AGs(object_name, username, password):
    pano = panorama.Panorama(hostname="10.60.198.122", api_username=username, api_password=password)
    device_groups = ["DeviceGroup1", "DeviceGroup2", "DeviceGroup3"]
    count = 0
    for device_group in device_groups:
        dg = panorama.DeviceGroup(device_group)
        pano.add(dg)
        AGs = objects.AddressGroup.refreshall(dg)
        for AG in AGs:
            if object_name in AG.static_value and len(AG.static_value) == 1:
                count = count + 1
                # check_in_shared_AGs(AG.name, username, password)
                # check_in_AGs(AG.name, username, password)
                # check_in_SRs(AG.name, username, password)
                # check_in_shared_SRs(AG.name, username, password)
            elif object_name in AG.static_value:
                count = count + 1
                # AG.static_value.remove(object_name)
                # AG.apply()
                # print(f"removed {object_name} from Address Group {AG.name} from {device_group} device group")
                # if AG.static_value == []:
                #     check_in_shared_AGs(AG.name, username, password)
                #     check_in_AGs(AG.name, username, password)
                #     check_in_SRs(AG.name, username, password)
                #     check_in_shared_SRs(AG.name, username, password)
                # else:
                #     continue
            else:
                continue
    return count

def check_in_SRs(object_name, username, password):
    pano = panorama.Panorama(hostname="10.60.198.122", api_username=username, api_password=password)
    device_groups = ["DeviceGroup1", "DeviceGroup2", "DeviceGroup3"]
    count = 0
    for device_group in device_groups:
        dg = panorama.DeviceGroup(device_group)
        pano.add(dg)
        rulebase = policies.PreRulebase()
        dg.add(rulebase)
        SecRules = policies.SecurityRule.refreshall(rulebase)
        for SecRule in SecRules:
            if (object_name in SecRule.source and len(SecRule.source) == 1) or (object_name in SecRule.destination and len(SecRule.destination) == 1):
                count = count + 1
                # rulebase.remove(SecRule)
                # rulebase.apply()
                # print(f"removed {SecRule.name} Security Rule on {device_group}")
            elif (object_name in SecRule.source) and (object_name in SecRule.destination):
                count = count + 1
                # SecRule.source.remove(object_name)
                # SecRule.destination.remove(object_name)
                # SecRule.apply()
                # print(f"removed {object_name} from the source and destination of {SecRule.name} Security Rule on {device_group}")
                # if(SecRule.source == []) or (SecRule.destination == []):
                #     rulebase.remove(SecRule)
                #     rulebase.apply()
                #     print(f"removed {SecRule.name} Security Rule on {device_group}")
                # else:
                #     continue
            elif object_name in SecRule.source:
                count = count + 1
                # SecRule.source.remove(object_name)
                # SecRule.apply()
                # print(f"removed {object_name} from the source of {SecRule.name} Security Rule on {device_group}")
                # if SecRule.source == []:
                #     rulebase.remove(SecRule)
                #     rulebase.apply()
                #     print(f"removed {SecRule.name} Security Rule on {device_group}")
                # else:
                #     continue
            elif object_name in SecRule.destination:
                count = count + 1
                # SecRule.destination.remove(object_name)
                # SecRule.apply()
                # print(f"removed {object_name} from the destination of {SecRule.name} Security Rule on {device_group}")
                # if SecRule.destination == []:
                #     rulebase.remove(SecRule)
                #     rulebase.apply()
                #     print(f"removed {SecRule.name} Security Rule on {device_group}")
                # else:
                #     continue
            else:
                continue
    return count 

def check_in_shared_SRs(object_name, username, password):
    pano = panorama.Panorama(hostname="10.60.198.122", api_username=username, api_password=password)
    rulebase = policies.PreRulebase()
    pano.add(rulebase)
    SecRules = policies.SecurityRule.refreshall(rulebase)
    count = 0
    for SecRule in SecRules:
        if (object_name in SecRule.source and len(SecRule.source) == 1) or (object_name in SecRule.destination and len(SecRule.destination) == 1):
            # rulebase.remove(SecRule)
            count = count + 1
            # rulebase.apply()
            # print(f"removed {SecRule.name} Security Rule on shared scope")
        elif (object_name in SecRule.source) and (object_name in SecRule.destination):
            count = count + 1
            # SecRule.source.remove(object_name)
            # SecRule.destination.remove(object_name)
            # SecRule.apply()
            # print(f"removed {object_name} from the source and destination of {SecRule.name} Security Rule on shared scope")
            # if(SecRule.source == []) or (SecRule.destination == []):
            #     rulebase.remove(SecRule)
            #     rulebase.apply()
            #     print(f"removed {SecRule.name} Security Rule on shared scope")
            # else:
            #     continue
        elif object_name in SecRule.source:
            count = count + 1
            # SecRule.source.remove(object_name)
            # SecRule.apply()
            # print(f"removed {object_name} from the source of {SecRule.name} Security Rule on shared scope")
            # if SecRule.source == []:
            #     rulebase.remove(SecRule)
            #     rulebase.apply()
            #     print(f"removed {SecRule.name} Security Rule on shared scope")
            # else:
            #     continue
        elif object_name in SecRule.destination:
            count = count + 1
            # SecRule.destination.remove(object_name)
            # SecRule.apply()
            # print(f"removed {object_name} from the destination of {SecRule.name} Security Rule on shared scope")
            # if SecRule.destination == []:
            #     rulebase.remove(SecRule)
            #     rulebase.apply()
            #     print(f"removed {SecRule.name} Security Rule on shared scope")
            # else:
            #     continue
        else:
            continue
    return count
 
def main():
    print("####___D E C O M M I S S I O N E R - Classic___####\nVersion-1.0\n")
    username = input("Please enter your username:  ")
    password = getpass.getpass("Please enter your password:  ")
    pano = panorama.Panorama(hostname="10.60.198.122", api_username=username, api_password=password)
    device_groups = ["DeviceGroup1", "DeviceGroup2", "DeviceGroup3"]
    unused_objects = []
    objfile = open('objects.csv','r')
    temp_list = csv.reader(objfile)
    for obj in temp_list:
        unused_objects.extend(obj)
    for unused_object in unused_objects:
        count = 0
        shared_objects = objects.AddressObject.refreshall(pano)
        for shared_object in shared_objects:
            if shared_object.value == unused_object:
                count = count + check_in_shared_AGs(shared_object.name, username, password)
                count = count + check_in_AGs(shared_object.name, username, password)
                count = count + check_in_SRs(shared_object.name, username, password)
                count = count + check_in_shared_SRs(shared_object.name, username, password)
                # shared_object.delete()
                # print(f"The object {shared_object.name} has been removed from Panorama")
            else:
                continue
        for device_group in device_groups:
            dg = panorama.DeviceGroup(device_group)
            pano.add(dg)
            decomm_objs = objects.AddressObject.refreshall(dg)
            for decomm_obj in decomm_objs:
                if decomm_obj.value == unused_object:
                    count = count + check_in_shared_AGs(decomm_obj.name, username, password)
                    count = count + check_in_AGs(decomm_obj.name, username, password)
                    count = count + check_in_SRs(decomm_obj.name, username, password)
                    count = count + check_in_shared_SRs(decomm_obj.name, username, password)
                    # dg.remove(decomm_obj)
                    # dg.apply()
                    # print(f"The object {decomm_obj.name} has been removed from Panorama")
                else:
                    continue
        if count != 0:
            print(f"{unused_object} is in use")
        else:
            print(f"{unused_object} is not in use")
                
if __name__ == "__main__":
    main()
