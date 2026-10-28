from __future__ import annotations


COMPONENTS = [
    {
        "name": "LM358",
        "category": "Op-Amp",
        "package": "Common: DIP-8 / SOIC-8",
        "summary": "Dual low-power operational amplifier that can run from a single supply and handle signals near ground.",
        "uses": ["Sensor signal conditioning", "Active filters", "Voltage followers", "Low-frequency gain stages"],
        "project_ideas": ["Battery monitor buffer", "Audio preamp experiment", "Light sensor threshold circuit"],
    },
    {
        "name": "LM324",
        "category": "Op-Amp",
        "package": "Common: DIP-14 / SOIC-14",
        "summary": "Quad low-power operational amplifier, useful when a design needs several basic analog stages.",
        "uses": ["Multi-channel sensor conditioning", "Filters", "Comparators at low speed", "Signal buffering"],
        "project_ideas": ["Four-channel sensor board", "Tone control circuit", "Window comparator prototype"],
    },
    {
        "name": "JRC4558",
        "category": "Op-Amp",
        "package": "Common: DIP-8 / SOIC-8",
        "summary": "Dual general-purpose op-amp often found in audio pedals, mixers, and older audio equipment.",
        "uses": ["Audio preamps", "Guitar pedal gain stages", "Active filters", "Tone shaping"],
        "project_ideas": ["Overdrive pedal", "Audio mixer channel strip", "Band-pass filter module"],
    },
    {
        "name": "NE5532",
        "category": "Op-Amp",
        "package": "Common: DIP-8 / SOIC-8",
        "summary": "Dual low-noise audio op-amp suited to line-level and higher-quality analog audio circuits.",
        "uses": ["Audio buffers", "Line preamps", "Active crossovers", "Low-noise filters"],
        "project_ideas": ["Headphone preamp front end", "Balanced audio receiver", "Low-noise filter test board"],
    },
    {
        "name": "LM386",
        "category": "Audio Amplifier",
        "package": "Common: DIP-8",
        "summary": "Low-voltage audio power amplifier for driving a small speaker from simple battery-powered circuits.",
        "uses": ["Small speaker amplifier", "Signal tracer", "Intercom circuits", "Portable audio experiments"],
        "project_ideas": ["Pocket amp", "Arduino tone speaker", "Bench audio probe"],
    },
    {
        "name": "TDA2030",
        "category": "Audio Amplifier",
        "package": "Common: TO-220-5",
        "summary": "Audio power amplifier IC for small speaker amps that need more output than an LM386-class circuit.",
        "uses": ["Small mono amplifiers", "Powered speaker modules", "Audio test loads", "Low-cost audio projects"],
        "project_ideas": ["Bench speaker amp", "Guitar practice amp", "Single-channel powered monitor"],
    },
    {
        "name": "TSA2822",
        "category": "Audio Amplifier",
        "package": "Common: DIP-8 / SOP-8",
        "summary": "Small dual audio amplifier. Verify the exact marking, because many parts in this role are TDA2822 variants.",
        "uses": ["Stereo headphone amp", "Small speaker driver", "Portable audio", "Signal monitor"],
        "project_ideas": ["Mini stereo amp", "Radio speaker output", "Audio test module"],
    },
    {
        "name": "UA741",
        "category": "Op-Amp",
        "package": "Common: DIP-8 / TO-99",
        "summary": "Classic single general-purpose op-amp, useful for learning and legacy circuits but not ideal for low-voltage single-supply work.",
        "uses": ["Educational op-amp circuits", "Legacy analog designs", "Basic filters", "Comparator demonstrations"],
        "project_ideas": ["Op-amp lab trainer", "Integrator/differentiator demo", "Basic active filter"],
    },
    {
        "name": "LM393",
        "category": "Comparator",
        "package": "Common: DIP-8 / SOIC-8",
        "summary": "Dual voltage comparator with open-collector outputs for threshold detection and logic interfacing.",
        "uses": ["Threshold detectors", "Zero-crossing detectors", "Sensor trip points", "Level conversion with pullups"],
        "project_ideas": ["Battery low-voltage alarm", "Light/dark switch", "RPM pulse conditioner"],
    },
    {
        "name": "LM339",
        "category": "Comparator",
        "package": "Common: DIP-14 / SOIC-14",
        "summary": "Quad open-collector voltage comparator for multi-threshold analog decision circuits.",
        "uses": ["Window comparators", "Multi-level indicators", "Sensor thresholds", "Oscillators"],
        "project_ideas": ["Battery level bar graph", "Four-sensor trip board", "Analog thermostat controller"],
    },
    {
        "name": "PC817",
        "category": "Optocoupler",
        "package": "Common: DIP-4",
        "summary": "Phototransistor optocoupler for simple signal isolation between low-voltage logic and noisy or separate circuits.",
        "uses": ["Logic isolation", "Mains detection with proper external parts", "Feedback isolation", "Ground-loop reduction"],
        "project_ideas": ["Isolated input module", "Relay feedback detector", "Microcontroller-safe signal interface"],
    },
    {
        "name": "CD4047",
        "category": "CMOS Logic",
        "package": "Common: DIP-14 / SOIC-14",
        "summary": "CMOS monostable/astable multivibrator used for timing, clock generation, and simple oscillator circuits.",
        "uses": ["Astable oscillators", "Monostable timers", "Inverter drive clocks", "Frequency generation"],
        "project_ideas": ["Simple square-wave generator", "Push-pull inverter clock", "Timer module"],
    },
    {
        "name": "CD4053",
        "category": "Analog Switch",
        "package": "Common: DIP-16 / SOIC-16",
        "summary": "Triple 2-channel analog multiplexer/demultiplexer for routing analog or digital signals.",
        "uses": ["Audio switching", "Signal routing", "ADC input selection", "Modulation experiments"],
        "project_ideas": ["Audio input selector", "Microcontroller-controlled signal router", "Sample-and-hold experiment"],
    },
    {
        "name": "NE555",
        "category": "Timer",
        "package": "Common: DIP-8 / SOIC-8",
        "summary": "General-purpose timer IC used for delays, oscillators, pulse generation, and simple waveform circuits.",
        "uses": ["Astable oscillator", "Monostable delay", "PWM dimmer", "Tone generator"],
        "project_ideas": ["LED flasher", "Simple servo tester", "Buzzer alarm", "Adjustable PWM controller"],
        "pins": [
            {"pin": "1", "name": "GND", "description": "Ground reference"},
            {"pin": "2", "name": "TRIG", "description": "Starts timing when pulled low"},
            {"pin": "3", "name": "OUT", "description": "Timer output"},
            {"pin": "4", "name": "RESET", "description": "Active-low reset"},
            {"pin": "5", "name": "CTRL", "description": "Control voltage input"},
            {"pin": "6", "name": "THRESH", "description": "Ends timing when above threshold"},
            {"pin": "7", "name": "DISCH", "description": "Discharge transistor connection"},
            {"pin": "8", "name": "VCC", "description": "Supply voltage"},
        ],
    },
    {
        "name": "PT2399",
        "category": "Audio Effect",
        "package": "Common: DIP-16",
        "summary": "Digital echo/delay processor commonly used in guitar pedals and simple audio delay circuits.",
        "uses": ["Echo effects", "Delay pedals", "Lo-fi audio delay", "Reverb-like effects"],
        "project_ideas": ["Guitar delay pedal", "Lo-fi vocal echo", "Dub delay module"],
    },
    {
        "name": "UC3842",
        "category": "Power Controller",
        "package": "Common: DIP-8 / SOIC-8",
        "summary": "Current-mode PWM controller commonly used in offline and DC-DC switching power supplies.",
        "uses": ["Flyback converters", "Boost converters", "Current-mode PWM control", "SMPS repair"],
        "project_ideas": ["Low-voltage boost converter study", "SMPS controller test jig", "Current-mode PWM demo"],
    },
    {
        "name": "UC3843",
        "category": "Power Controller",
        "package": "Common: DIP-8 / SOIC-8",
        "summary": "Current-mode PWM controller similar to UC3842, often used where lower startup thresholds are useful.",
        "uses": ["DC-DC converters", "Flyback supplies", "PWM gate drive control", "Power supply experiments"],
        "project_ideas": ["Boost converter controller", "Bench SMPS trainer", "MOSFET gate drive experiment"],
    },
    {
        "name": "ULN2003",
        "category": "Driver Array",
        "package": "Common: DIP-16 / SOIC-16",
        "summary": "Seven-channel Darlington transistor array for driving relays, lamps, solenoids, and stepper coils.",
        "uses": ["Relay drivers", "Unipolar stepper motors", "LED loads", "Solenoid drivers"],
        "project_ideas": ["Stepper motor driver board", "Relay output module", "Microcontroller load driver"],
    },
    {
        "name": "ULN2803",
        "category": "Driver Array",
        "package": "Common: DIP-18 / SOIC-18",
        "summary": "Eight-channel Darlington transistor array for sinking moderate-current loads from logic outputs.",
        "uses": ["Relay banks", "LED matrices", "Solenoids", "Logic-to-load interfaces"],
        "project_ideas": ["8-channel relay board", "LED matrix sink driver", "Automation output module"],
    },
    {
        "name": "7660",
        "category": "Power Converter",
        "package": "Common: DIP-8 / SOIC-8",
        "summary": "Switched-capacitor voltage converter often used to generate a negative rail from a positive supply.",
        "uses": ["Charge pumps", "Negative op-amp rails", "Small voltage inversion", "Low-current split supplies"],
        "project_ideas": ["Op-amp negative rail module", "Portable audio bias supply", "Charge-pump demo board"],
    },
]


for part in [
    "IRFZ44N",
    "IRF530N",
    "IRF540N",
    "IRF640N",
    "IRF740N",
    "IRF840N",
    "RFP30N06LE",
    "2N7000",
    "IRF3025",
]:
    COMPONENTS.append(
        {
            "name": part,
            "category": "N-Channel MOSFET",
            "package": "Verify package marking",
            "summary": "N-channel MOSFET for switching and power control. Check the exact datasheet for voltage, current, gate threshold, and safe operating area.",
            "uses": ["Low-side switching", "Motor control", "LED dimming", "DC load control", "Switch-mode power stages"],
            "project_ideas": ["PWM LED dimmer", "DC motor speed controller", "Microcontroller low-side switch"],
        }
    )

COMPONENTS.append(
    {
        "name": "IRF9540",
        "category": "P-Channel MOSFET",
        "package": "Common: TO-220",
        "summary": "P-channel power MOSFET commonly used for high-side switching and reverse-polarity protection experiments.",
        "uses": ["High-side switching", "Power path control", "Reverse polarity protection", "Battery load switching"],
        "project_ideas": ["High-side load switch", "Protected battery input", "H-bridge study with complementary MOSFETs"],
    }
)

LS_LOGIC = {
    "74LS00": "Quad 2-input NAND gate.",
    "74LS02": "Quad 2-input NOR gate.",
    "74LS04": "Hex inverter.",
    "74LS08": "Quad 2-input AND gate.",
    "74LS32": "Quad 2-input OR gate.",
    "74LS47": "BCD to seven-segment display driver for common-anode displays.",
    "74LS74": "Dual D-type flip-flop.",
    "74LS86": "Quad 2-input XOR gate.",
    "74LS90": "Decade counter.",
    "74LS138": "3-to-8 line decoder/demultiplexer.",
    "74LS164": "8-bit serial-in parallel-out shift register.",
    "74LS245": "Octal bus transceiver.",
}

HC_LOGIC = {
    "74HC00": "Quad 2-input NAND gate.",
    "74HC02": "Quad 2-input NOR gate.",
    "74HC04": "Hex inverter.",
    "74HC08": "Quad 2-input AND gate.",
    "74HC14": "Hex Schmitt-trigger inverter.",
    "74HC32": "Quad 2-input OR gate.",
    "74HC138": "3-to-8 line decoder/demultiplexer.",
    "74HC164": "8-bit serial-in parallel-out shift register.",
    "74HC165": "8-bit parallel-in serial-out shift register.",
    "74HC595": "8-bit serial-in parallel-out shift register with output latch.",
}

for family, parts in [("74LS TTL Logic", LS_LOGIC), ("74HC CMOS Logic", HC_LOGIC)]:
    for name, description in parts.items():
        COMPONENTS.append(
            {
                "name": name,
                "category": family,
                "package": "Common: DIP / SOIC",
                "summary": description,
                "uses": ["Digital logic building blocks", "Address decoding", "Counters and registers", "Glue logic"],
                "project_ideas": ["Logic trainer module", "Breadboard computer circuit", "LED/display controller", "Microcontroller I/O expansion"],
            }
        )


def pins(names):
    return [{"pin": str(index), "name": name, "description": description_for_pin(name)} for index, name in enumerate(names, 1)]


def description_for_pin(name):
    if name in {"GND", "VSS"}:
        return "Ground reference"
    if name in {"VCC", "VDD"}:
        return "Positive supply"
    if name in {"V+", "VS+"}:
        return "Positive supply rail"
    if name in {"V-", "VS-"}:
        return "Negative supply rail or ground in single-supply circuits"
    if name in {"NC"}:
        return "No internal connection"
    if name.startswith("Y") or name.endswith("Y") or name in {"Q", "QA", "QB", "QC", "QD", "QE", "QF", "QG", "QH", "QH'", "OUT"}:
        return "Output"
    if name.startswith("A") or name.startswith("B") or name in {"D", "CLK", "CLR", "PRE", "RESET", "TRIG", "THRESH"}:
        return "Input"
    return ""


OP_AMP_PINOUTS = {
    "dual": pins(["OUT A", "-IN A", "+IN A", "V-", "+IN B", "-IN B", "OUT B", "V+"]),
    "quad": pins(["OUT 1", "-IN 1", "+IN 1", "V+", "+IN 2", "-IN 2", "OUT 2", "OUT 3", "-IN 3", "+IN 3", "V-", "+IN 4", "-IN 4", "OUT 4"]),
    "single": pins(["OFFSET NULL", "-IN", "+IN", "V-", "OFFSET NULL", "OUT", "V+", "NC"]),
}

COMMON_PINOUTS = {
    "LM358": OP_AMP_PINOUTS["dual"],
    "JRC4558": OP_AMP_PINOUTS["dual"],
    "NE5532": OP_AMP_PINOUTS["dual"],
    "LM324": OP_AMP_PINOUTS["quad"],
    "UA741": OP_AMP_PINOUTS["single"],
    "LM386": pins(["GAIN", "-IN", "+IN", "GND", "VOUT", "VS", "BYPASS", "GAIN"]),
    "TDA2030": pins(["NON-INVERTING IN", "INVERTING IN", "V-", "OUT", "V+"]),
    "TSA2822": pins(["OUT 1", "VCC", "OUT 2", "GND", "IN 2+", "IN 2-", "IN 1+", "IN 1-"]),
    "LM393": pins(["OUT 1", "-IN 1", "+IN 1", "GND", "+IN 2", "-IN 2", "OUT 2", "VCC"]),
    "LM339": pins(["OUT 2", "OUT 1", "VCC", "-IN 1", "+IN 1", "-IN 2", "+IN 2", "-IN 3", "+IN 3", "-IN 4", "+IN 4", "GND", "OUT 4", "OUT 3"]),
    "PC817": pins(["ANODE", "CATHODE", "EMITTER", "COLLECTOR"]),
    "CD4047": pins(["C", "R", "RC COMMON", "ASTABLE", "ASTABLE", "-TRIGGER", "+TRIGGER", "VSS", "EXT RESET", "Q", "NOT Q", "RETRIGGER", "OSC OUT", "VDD"]),
    "CD4053": pins(["Y0", "Y1", "Y", "Z", "Z1", "Z0", "INH", "VSS", "C", "B", "A", "X0", "X", "X1", "VEE", "VDD"]),
    "NE555": pins(["GND", "TRIG", "OUT", "RESET", "CTRL", "THRESH", "DISCH", "VCC"]),
    "PT2399": pins(["VCC", "REF", "AGND", "DGND", "CLK_O", "VCO", "CC1", "CC0", "OP1-OUT", "OP1-IN", "OP2-IN", "OP2-OUT", "LPF2-IN", "LPF2-OUT", "LPF1-OUT", "LPF1-IN"]),
    "UC3842": pins(["COMP", "VFB", "ISENSE", "RT/CT", "GND", "OUT", "VCC", "VREF"]),
    "UC3843": pins(["COMP", "VFB", "ISENSE", "RT/CT", "GND", "OUT", "VCC", "VREF"]),
    "ULN2003": pins(["1B", "2B", "3B", "4B", "5B", "6B", "7B", "GND", "COM", "7C", "6C", "5C", "4C", "3C", "2C", "1C"]),
    "ULN2803": pins(["1B", "2B", "3B", "4B", "5B", "6B", "7B", "8B", "GND", "COM", "8C", "7C", "6C", "5C", "4C", "3C", "2C", "1C"]),
    "7660": pins(["BOOST", "CAP+", "GND", "CAP-", "VOUT", "LV", "OSC", "V+"]),
}

MOSFET_PINOUT = [
    {"pin": "1", "name": "GATE", "description": "Common TO-220 front-view pin 1; verify exact package datasheet"},
    {"pin": "2", "name": "DRAIN", "description": "Common TO-220 front-view pin 2 and tab; verify exact package datasheet"},
    {"pin": "3", "name": "SOURCE", "description": "Common TO-220 front-view pin 3; verify exact package datasheet"},
]

LOGIC_PINOUTS = {
    "quad_2_input": pins(["1A", "1B", "1Y", "2A", "2B", "2Y", "GND", "3Y", "3A", "3B", "4Y", "4A", "4B", "VCC"]),
    "hex_inverter": pins(["1A", "1Y", "2A", "2Y", "3A", "3Y", "GND", "4Y", "4A", "5Y", "5A", "6Y", "6A", "VCC"]),
    "ls47": pins(["B", "C", "LT", "BI/RBO", "RBI", "D", "A", "GND", "e", "d", "c", "b", "a", "g", "f", "VCC"]),
    "ls74": pins(["1CLR", "1D", "1CLK", "1PRE", "1Q", "1NOT Q", "GND", "2NOT Q", "2Q", "2PRE", "2CLK", "2D", "2CLR", "VCC"]),
    "ls90": pins(["CLK A", "RESET 1", "RESET 2", "NC", "VCC", "RESET 3", "RESET 4", "QC", "QB", "GND", "QD", "QA", "NC", "CLK B"]),
    "decoder_138": pins(["A", "B", "C", "G2A", "G2B", "G1", "Y7", "GND", "Y6", "Y5", "Y4", "Y3", "Y2", "Y1", "Y0", "VCC"]),
    "shift_164": pins(["A", "B", "QA", "QB", "QC", "QD", "GND", "CLK", "CLR", "QE", "QF", "QG", "QH", "VCC"]),
    "ls245": pins(["DIR", "A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "GND", "B8", "B7", "B6", "B5", "B4", "B3", "B2", "B1", "OE", "VCC"]),
    "hc165": pins(["SH/LD", "CLK", "E", "F", "G", "H", "QH", "GND", "QH'", "SER", "A", "B", "C", "D", "CLK INH", "VCC"]),
    "hc595": pins(["QB", "QC", "QD", "QE", "QF", "QG", "QH", "GND", "QH'", "SRCLR", "SRCLK", "RCLK", "OE", "SER", "QA", "VCC"]),
}

LOGIC_DETAILS = {
    "00": ("quad_2_input", "NAND gate", ["Universal logic construction", "Enable/disable logic", "Latch building blocks"], ["Build an SR latch", "Create any basic gate from NANDs", "Button debounce latch"]),
    "02": ("quad_2_input", "NOR gate", ["Universal logic construction", "Reset-dominant latch circuits", "Simple control logic"], ["Build an SR latch", "Create a NOR-only logic trainer", "Power-on reset gate"]),
    "04": ("hex_inverter", "inverter", ["Signal inversion", "Clock buffering", "Oscillator experiments"], ["Blinker oscillator", "Logic probe inverter stage", "Clock fanout buffer"]),
    "08": ("quad_2_input", "AND gate", ["Enable gating", "Address qualification", "State-machine logic"], ["Chip-select qualifier", "Two-condition alarm", "Counter reset gate"]),
    "32": ("quad_2_input", "OR gate", ["Combining logic conditions", "Interrupt request combining", "Control gating"], ["Multi-source event detector", "Simple priority input combiner", "Alarm input combiner"]),
    "86": ("quad_2_input", "XOR gate", ["Parity generation", "Phase comparison", "Controlled inversion"], ["Parity checker", "Half-adder demo", "Digital phase detector"]),
    "47": ("ls47", "BCD to seven-segment display driver", ["Driving common-anode seven-segment displays", "Counter displays", "BCD readouts"], ["One-digit counter display", "DIP-switch numeric display", "Frequency counter display stage"]),
    "74": ("ls74", "dual D flip-flop", ["State storage", "Frequency division", "Edge-triggered control"], ["Divide-by-two clock", "Toggle latch", "Simple state machine"]),
    "90": ("ls90", "decade counter", ["Decimal counting", "Clock division", "Event counting"], ["0-9 LED counter", "Seconds counter stage", "Frequency divider"]),
    "138": ("decoder_138", "3-to-8 decoder/demultiplexer", ["Address decoding", "One-of-eight selection", "Chip select generation"], ["Memory address decoder", "LED scanner", "One-of-eight relay selector"]),
    "164": ("shift_164", "serial-in parallel-out shift register", ["Serial to parallel expansion", "LED driving", "Bit pattern generation"], ["LED chaser", "Simple serial display output", "Logic analyzer pattern source"]),
    "245": ("ls245", "octal bus transceiver", ["Bidirectional bus buffering", "Data bus isolation", "Level-family interfacing with care"], ["Breadboard computer data bus", "Bus isolation board", "8-bit diagnostic breakout"]),
    "14": ("hex_inverter", "Schmitt-trigger inverter", ["Noisy signal cleanup", "RC oscillators", "Button debounce"], ["Debounced button input", "RC clock oscillator", "Slow-edge sensor conditioner"]),
    "165": ("hc165", "parallel-in serial-out shift register", ["Reading many digital inputs", "Keyboard scanning", "Switch banks"], ["8-button input expander", "DIP-switch reader", "Parallel sensor snapshot"]),
    "595": ("hc595", "serial-in parallel-out register with latch", ["Microcontroller output expansion", "LED/display driving", "Latched control outputs"], ["8-output LED module", "Seven-segment digit driver", "Relay control expander"]),
}

DATASHEETS = {
    "LM358": "https://www.ti.com/lit/ds/symlink/lm358.pdf",
    "LM324": "https://www.ti.com/lit/ds/symlink/lm324.pdf",
    "JRC4558": "https://www.njr.com/electronic_device/PDF/NJM4558_NJM4559_E.pdf",
    "NE5532": "https://www.ti.com/lit/ds/symlink/ne5532.pdf",
    "LM386": "https://www.ti.com/lit/ds/symlink/lm386.pdf",
    "TDA2030": "https://www.st.com/resource/en/datasheet/tda2030.pdf",
    "TSA2822": "https://www.st.com/resource/en/datasheet/tda2822d.pdf",
    "UA741": "https://www.ti.com/lit/ds/symlink/ua741.pdf",
    "LM393": "https://www.ti.com/lit/ds/symlink/lm393.pdf",
    "LM339": "https://www.ti.com/lit/ds/symlink/lm339.pdf",
    "PC817": "https://www.vishay.com/docs/83522/pc817.pdf",
    "CD4047": "https://www.ti.com/lit/ds/symlink/cd4047b.pdf",
    "CD4053": "https://www.ti.com/lit/ds/symlink/cd4053b.pdf",
    "NE555": "https://www.ti.com/lit/ds/symlink/ne555.pdf",
    "PT2399": "https://electricdruid.net/datasheets/PT2399.pdf",
    "UC3842": "https://www.ti.com/lit/ds/symlink/uc3842.pdf",
    "UC3843": "https://www.ti.com/lit/ds/symlink/uc3843.pdf",
    "ULN2003": "https://www.ti.com/lit/ds/symlink/uln2003a.pdf",
    "ULN2803": "https://www.ti.com/lit/ds/symlink/uln2803a.pdf",
    "7660": "https://www.ti.com/lit/ds/symlink/lmc7660.pdf",
    "IRFZ44N": "https://www.alldatasheet.com/datasheet-pdf/pdf/68619/IRF/IRFZ44N.html",
    "IRF530N": "https://www.alldatasheet.com/view.jsp?Searchword=IRF530N",
    "IRF540N": "https://www.alldatasheet.com/view.jsp?Searchword=IRF540N",
    "IRF640N": "https://www.alldatasheet.com/view.jsp?Searchword=IRF640N",
    "IRF740N": "https://www.alldatasheet.com/view.jsp?Searchword=IRF740N",
    "IRF840N": "https://www.alldatasheet.com/view.jsp?Searchword=IRF840N",
    "RFP30N06LE": "https://www.alldatasheet.com/datasheet-pdf/pdf/118243/FAIRCHILD/RFP30N06LE.html",
    "2N7000": "https://www.alldatasheet.com/view.jsp?Searchword=2N7000",
    "IRF3025": "https://www.alldatasheet.com/view.jsp?Searchword=IRF3025",
    "IRF9540": "https://www.alldatasheet.com/view.jsp?Searchword=IRF9540",
}


def logic_suffix(name):
    return name.removeprefix("74LS").removeprefix("74HC")


def enrich_components():
    for component in COMPONENTS:
        name = component["name"]
        if name in COMMON_PINOUTS:
            component["pins"] = COMMON_PINOUTS[name]
        if name in DATASHEETS:
            component["datasheet_url"] = DATASHEETS[name]
        if component["category"] in {"N-Channel MOSFET", "P-Channel MOSFET"}:
            component["pins"] = MOSFET_PINOUT
            component["model_type"] = "mosfet_to220_3pin"
            component["notes"] = "Pinout shown is the common TO-220 front-view convention. Verify the exact manufacturer datasheet and package before wiring."
        if name.startswith(("74LS", "74HC")):
            suffix = logic_suffix(name)
            key, device, uses, ideas = LOGIC_DETAILS[suffix]
            family = "TTL" if name.startswith("74LS") else "CMOS"
            component["summary"] = f"{family} {device}."
            component["uses"] = uses
            component["project_ideas"] = ideas
            component["pins"] = LOGIC_PINOUTS[key]
            component["model_type"] = f"dip_{len(component['pins']):02d}"
            component["datasheet_url"] = f"https://www.ti.com/lit/ds/symlink/sn{name.lower()}.pdf"

        if "model_type" not in component and component.get("pins") and len(component["pins"]) in {4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28}:
            component["model_type"] = f"dip_{len(component['pins']):02d}"


enrich_components()
