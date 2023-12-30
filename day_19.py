from aocd import get_data
import copy
from collections import deque
from pprint import PrettyPrinter

real_data = get_data(day=19, year=2023).splitlines()
data2 = [
    "px{a<2006:qkq,m>2090:A,rfg}",
    "pv{a>1716:R,A}",
    "lnx{m>1548:A,A}",
    "rfg{s<537:gd,x>2440:R,A}",
    "qs{s>3448:A,lnx}",
    "qkq{x<1416:A,crn}",
    "crn{x>2662:A,R}",
    "in{s<1351:px,qqz}",
    "qqz{s>2770:qs,m<1801:hdj,R}",
    "gd{a>3333:R,R}",
    "hdj{m>838:A,pv}",
    "",
    "{x=787,m=2655,a=1222,s=2876}",
    "{x=1679,m=44,a=2067,s=496}",
    "{x=2036,m=264,a=79,s=2244}",
    "{x=2461,m=1339,a=466,s=291}",
    "{x=2127,m=1623,a=2188,s=1013}",
]

data = real_data


def make_item(l):
    l = {v[0]: int(v[2:]) for v in l.strip("{").strip("}").split(",")}
    return l


def make_rule(r):
    rule_key = r.split("{")[0]
    rules = r.split("{")[1].strip("}").split(",")
    default_action = rules[-1]
    rules = rules[:-1]
    rule_dict = {i.split(":")[0]: i.split(":")[1] for i in rules}
    return (rule_key, (rule_dict, default_action))


def process_rule(x, m, a, s, rule_key, rules):
    for k, v in rules[rule_key][0].items():
        if eval(k):
            match v:
                case "R":
                    return 0
                case "A":
                    return x + m + a + s
                case _:
                    return process_rule(x, m, a, s, v, rules)
    match rules[rule_key][1]:
        case "R":
            return 0
        case "A":
            return x + m + a + s
        case _ as new_rule:
            return process_rule(x, m, a, s, new_rule, rules)


def part_1():
    pp = PrettyPrinter()
    rules = {key: value for i in data[: data.index("")] for key, value in [make_rule(i)]}
    items = [make_item(i) for i in data[data.index("") + 1 :]]
    retval = 0
    for i in items:
        retval += process_rule(i["x"], i["m"], i["a"], i["s"], "in", rules)
    return retval


def part_2():
    pp = PrettyPrinter()
    rules = {key: value for i in data[: data.index("")] for key, value in [make_rule(i)]}
    d = deque()
    final_a = deque()
    final_r = deque()
    d.append(
        [
            "in",
            {
                "x_gt": 0,
                "x_lt": 4001,
                "m_gt": 0,
                "m_lt": 4001,
                "a_gt": 0,
                "a_lt": 4001,
                "s_gt": 0,
                "s_lt": 4001,
            }
        ]
    )
    while d:
        node = d.pop()
        if node[0] == 'A':
            final_a.append(copy.deepcopy(node))
            continue
        if node[0] == 'R':
            final_r.append(copy.deepcopy(node))
            continue
        # Need to process each rule in order.
        # Any with A are finalized
        # Any with R are finalized
        # Any with "something" require us to spawn two new rules.  One that "follows" the rule to the next rule,
        #    and one that is opposite the rule and falls to the next rule to be applied.
        new_dict = copy.deepcopy(node[1])
        for k,v in rules[node[0]][0].items():
            var = k[0] + '_'
            op = (('lt','gt') if k[1] == '<' else ('gt','lt'))
            i = int(k[2:])
            if op == ('lt','gt'):
                # less than is positive
                if new_dict[var+op[0]] <= i:
                    # the current node value is less than the value in the rule, then just requeue the node with the new rule.
                    d.append([v,copy.deepcopy(new_dict)])
                else:
                    # the current node value is greater than the value in the rule,
                    # so we enqueue a positive, and fall through a negative.
                    new_dict1 = copy.deepcopy(new_dict)
                    new_dict1[var+op[0]] = i
                    d.append([v, new_dict1])
                    new_dict2 = copy.deepcopy(new_dict)
                    new_dict2[var+op[1]] = i - 1
                    new_dict = new_dict2
            else: # ('gt','lt')
                # greater than is positive
                if new_dict[var+op[0]] >= i:
                    # the current node value is greater than the value in the rule, then just requeue the node with the new rule.
                    d.append([v,copy.deepcopy(new_dict)])
                else:
                    # the current node value is less than the value in the rule,
                    # so we enqueue a positive, and fall through a negative.
                    new_dict1 = copy.deepcopy(new_dict)
                    new_dict1[var+op[0]] = i
                    d.append([v, new_dict1])
                    new_dict2 = copy.deepcopy(new_dict)
                    new_dict2[var+op[1]] = i + 1
                    new_dict = new_dict2
        d.append([rules[node[0]][1], new_dict])    
    retval = 0
    while(final_a):
        r = final_a.pop()
        x_count = r[1]['x_lt'] - (r[1]['x_gt']+1)
        m_count = r[1]['m_lt'] - (r[1]['m_gt']+1)
        a_count = r[1]['a_lt'] - (r[1]['a_gt']+1)
        s_count = r[1]['s_lt'] - (r[1]['s_gt']+1)
        retval += x_count * m_count * a_count * s_count
    return retval



print(f"Part 1: {part_1()}, Part 2: {part_2()}")
