from aocd import get_data
from aoc_utils import lcm
from collections import deque

real_data = get_data(day=20, year=2023).splitlines()
m_dict = dict()

def get_module(name: str):
    global m_dict
    return m_dict[name]

def module_factory(line: str):
    match line[0]:
        case 'b':
            m = Broadcaster(line)
        case '%':
            m = Flipflop(line)
        case '&':
            m = Conjunction(line)
    return (m.name, m)

class Module():
    def __init__(self, name: str) -> None:
        self.name = name
        self.outputs = []
        self.inputs_list = []
        

    def setup_as_input_for_outputs(self):
        global m_dict
        for o in self.outputs:
            m_dict[o].setup_input(self.name)    
    
    def setup_input(self, line: str):
        self.inputs_list.append(line)
    
    def setup_outputs(self, line: str):
        outputs = [o.strip(',') for o in line.split()[2:]]
        self.outputs = outputs
        
    def process_pulse(self, input, pulse_val):
        return []
    
class Broadcaster(Module): 
    def __init__(self, line: str) -> None:
        super().__init__(line.split()[0])
        super().setup_outputs(line)
    
    def process_pulse(self, input, pulse_val):
        return [(o, self.name, pulse_val) for o in self.outputs]
        
    
class Flipflop(Module):
    def __init__(self, line: str) -> None:
        super().__init__(line.split()[0][1:])
        super().setup_outputs(line)
        self.state = False
    
    def process_pulse(self, input, pulse_val):
        if pulse_val: # Flipflop does nothing on "high" pulse
            return []
        self.state = not self.state
        return [(o, self.name, self.state) for o in self.outputs]
        

class Conjunction(Module):
    def __init__(self, line: str) -> None:
        super().__init__(line.split()[0][1:])
        super().setup_outputs(line)
        self.inputs = {}
        
    def setup_input(self, input: str):
        super().setup_input(input)
        self.inputs[input] = False

    def process_pulse(self, input, pulse_val):
        self.inputs[input] = pulse_val
        val_to_send = not all(self.inputs.values())
        return [(o, self.name, val_to_send) for o in self.outputs]
        

class Button(Module):
    def __init__(self, line: str) -> None:
        super().__init__('Button')
        self.outputs.append('broadcaster')

    def process_pulse(self, input, pulse_val):
        return [(o, self.name, pulse_val) for o in self.outputs]
    
class Sink(Module):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def process_pulse(self, input, pulse_val):
        return []
    
                    
data = real_data

def part_1():
    global m_dict
    m_dict = {k:v for l in data for k,v in [module_factory(l)]}
    for l in data:
        outputs = [o.strip(',') for o in l.split()[2:]]
        for o in outputs:
            if o not in m_dict.keys():
                m_dict[o] = Sink(o)
        
    m_dict['button'] = Button('')
    for k,v in m_dict.items():
        v.setup_as_input_for_outputs()
    
    low_pulses = 0
    high_pulses = 0
    loop_count = 1000
    d = deque()
    for i in range(loop_count):
        d.append(('button','', False))
        while d:
            pulse = d.popleft()
            low_pulses += 1 if not pulse[2] else 0
            high_pulses += 1 if pulse[2] else 0
            new_p = m_dict[pulse[0]].process_pulse(pulse[1], pulse[2])
            for p in new_p:
                d.append(p)
    return high_pulses * (low_pulses - loop_count)    

def part_2():
    global m_dict
    m_dict = {k:v for l in data for k,v in [module_factory(l)]}
    for l in data:
        outputs = [o.strip(',') for o in l.split()[2:]]
        for o in outputs:
            if o not in m_dict.keys():
                m_dict[o] = Sink(o)
        
    m_dict['button'] = Button('')
    for k,v in m_dict.items():
        v.setup_as_input_for_outputs()

    loop_count = 4096
    d = deque()
    cycles = []
    for i in range(loop_count):
        d.append(('button','', False))
        while d:
            pulse = d.popleft()
            new_p = m_dict[pulse[0]].process_pulse(pulse[1], pulse[2])
            for p in new_p:
                d.append(p)
        if not any(m_dict['xq'].inputs.values()) and not any([m_dict['zl'].state, m_dict['cx'].state, m_dict['qh'].state, m_dict['hs'].state]):
            cycles.append(i+1)
        if not any(m_dict['vv'].inputs.values()) and not any([m_dict['br'].state, m_dict['mm'].state, m_dict['tr'].state]):
            cycles.append(i+1)
        if not any(m_dict['dv'].inputs.values()) and not any([m_dict['hx'].state, m_dict['bl'].state, m_dict['fd'].state]):
            cycles.append(i+1)
        if not any(m_dict['jc'].inputs.values()) and not any([m_dict['ps'].state, m_dict['xv'].state]):
            cycles.append(i+1)

    return lcm(cycles)


print(f"Part 1: {part_1()} Part 2: {part_2()}")
