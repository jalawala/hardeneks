from importlib import import_module
import hardeneks


def harden(resources, config, _type):
    config = config[_type]
    results = []
    #pillarsList = get_pillars_list()
    print("pillarsList={} in hardeneks".format(hardeneks.pillarsList))
    
    for pillar in config.keys():
        print("pillar={}".format(pillar))
        if pillar in hardeneks.pillarsList:
            for section in config[pillar]:
                for rule in config[pillar][section]:
                    module = import_module(f"hardeneks.{_type}.{pillar}.{section}")
                    try:
                        cls = getattr(module, rule)
                        print("cls={}".format(cls))
                    except AttributeError as exc:
                        print(f"[bold][red]{exc}")
                    try:
                        rule = cls()
                        rule.check(resources)
                        results.append(rule)
                    except Exception as exc:
                        print(f"[bold][red]{exc}")

    return results
