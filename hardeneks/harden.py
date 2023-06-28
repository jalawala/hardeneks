from importlib import import_module
import hardeneks


def harden(resources, rulesMap, _type):
    config = rulesMap[_type]
    results = []
    #pillarsList = get_pillars_list()
    #print("pillarsList={} in hardeneks".format(hardeneks.pillarsList))
    
    for pillar in config.keys():
        #print("pillar={} _type={}".format(pillar, _type))
        if pillar in hardeneks.pillarsList:
            for section in config[pillar]:
                if section in hardeneks.sectionsMap[pillar]:
                    
                    if hardeneks.rulesList:
                        selectedRulesList = hardeneks.rulesList
                    else:
                        selectedRulesList = config[pillar][section]    
                    
                    for rule in selectedRulesList:
                        #print("Checking rule={} section={} pillar={} scope={}".format(rule, section, pillar, _type))
                        module = import_module(f"hardeneks.{_type}.{pillar}.{section}")
                        try:
                            cls = getattr(module, rule)
                            #print("cls={}".format(cls))
                        #except AttributeError as exc:
                        #    print(f"[bold][red]{exc}")
                        except Exception as exc:
                            if _type == "cluster_wide":
                                print(f"AttributeError for rule {rule} in Section {section} for Pillar {pillar} for scope {_type}: [bold][red]{exc}")
                            else:
                                print(f"AttributeError for rule {rule} in Section {section} for Pillar {pillar} for scope {_type} for namespace: {resources.namespace}: [bold][red]{exc}")
                        try:
                            ruleObject = cls()
                            ruleObject.name = rule
                            ruleObject.check(resources)
                            results.append(ruleObject)
                        #except Exception as exc:
                        #    print(f"[bold][red]{exc}")
                        except Exception as exc:
                            if _type == "cluster_wide":
                                print(f"Exception for rule {rule} in Section {section} for Pillar {pillar} for scope {_type}: [bold][red]{exc}")
                            else:
                                print(f"Exception for rule {rule} in Section {section} for Pillar {pillar} for scope {_type} for namespace: {resources.namespace}: [bold][red]{exc}")
                                                                      

    return results
