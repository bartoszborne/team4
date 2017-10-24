import mapstructure as map_s
import player


def print_city_map(police_visible, hospital_visible, shipping_visible, victim_visible):
    if police_visible:
        print_police = [" Police Station ", "      ╔═╗       ", "      ╚═╝       "]
    else:
        print_police = ["                ", "                ", "                "]

    if hospital_visible:
        print_hospital = ["    Hospital    ", "      ╔═╗       ", "      ╚═╝       "]
    else:
        print_hospital = ["                ", "                ", "                "]

    if shipping_visible:
        print_shipping = ["Shipping Company", "      ╔═╗       ", "      ╚═╝       "]
    else:
        print_shipping = ["                ", "                ", "                "]

    if victim_visible:
        print_victim = ["  Joe's House   ", "      ╔═╗       ", "      ╚═╝       "]
    else:
        print_victim = ["                ", "                ", "                "]
    
    city_map = """
╔═════════════════════════ CITY MAP - BUILDINGS ═════════════════════════╗
║                                                ▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓║
║                                                     ▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓║
║     %s                                   ▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓║
║     %s                                        ▒▒▒▒▒▒▒▒▓▓▓║
║     %s                                            ▒▒▒▒▒▓▓║
║                                        %s        ▒▒▒▒▒▓▓▓║
║                                        %s        ▒▒▒▒▒▒▓▓║
║                                        %s         ▒▒▒▒▒▒▓║
║                                                                     ▒▒▒║
║                                                                       ▒║
║\_                                                                      ║
║░░\                                                                     ║
║░░░|                                                                    ║
║░░/                                             %s        ║
║░|   %s                           %s        ║
║░░\  %s                           %s        ║
║░░░\_%s                                                   ║
║░░░░░\____                                                              ║
║░░░░░░░░░░\                                                             ║
╚════════════════════════════════════════════════════════════════════════╝""" % (print_hospital[0], print_hospital[1], print_hospital[2],
    print_police[0], print_police[1], print_police[2],
    print_victim[0], print_shipping[0], print_victim[1], print_shipping[1], print_victim[2], print_shipping[2])

    print(city_map)


def print_building_map(building):
    if building == "Police Station":
        print("""
╔════════════════════════ POLICE STATION - ROOMS ════════════════════════╗
║ ╔═════════════════════╗ ╔══════════════════╗       ╔═════════════════╗ ║
║ ║ Jail Room           ║ ║ Interrogation    ║       ║ Chief's Office  ║ ║
║ ║                     ║ ║ Room             ║ ┌─────╝                 ║ ║
║ ║                     ║ ║                  ║ │                       ║ ║
║ ║                     ║ ║                  ║ │  ┌──╗                 ║ ║
║ ║                     ║ ║                  ║ │  │  ║                 ║ ║
║ ║                     ║ ║                  ║ │  │  ╚═════════════════╝ ║
║ ╚════════╗  ╔═════════╝ ╚═══════╗  ╔═══════╝ │  │                      ║
║          │  └───────────────────┘  └─────────┘  └───┐ ╔══════════════╗ ║
║          │                                          │ ║ My Office    ║ ║
║          │  ┌────────────────────────────────────┐  └─╝              ║ ║
║ ╔════════╝  ╚════════╗                           │                   ║ ║
║ ║ Police Lobby       ║                           │  ┌─╗              ║ ║
║ ║                    ║                           │  │ ╚══════════════╝ ║
║ ║                    ║                           │  │ ╔══════════════╗ ║
║ ║                    ║                           │  │ ║ Joe's Office ║ ║
║ ║                    ║                           │  └─╝              ║ ║
║ ║                    ║                           │                   ║ ║
║ ║                    ║                           └────╗              ║ ║
║ ╚════════╗  ╔════════╝                                ╚══════════════╝ ║
╚══════════╝  ╚══════════════════════════════════════════════════════════╝""")

    elif building == "Hospital":
        print("""
╔═══════════════════════════ HOSPITAL - ROOMS ═══════════════════════════╗
║ ╔══════════════╗                                                       ║
║ ║ Patient's    ║                                                       ║
║ ║ Room (Joe)   ║                                                       ║
║ ║              ║                                   ╔═════════════════╗ ║
║ ║              ║                                   ║ Surveillance    ║ ║
║ ╚╗  ╔══════════╝                           ┌───────╝ Room            ║ ║
║  │  │                                      │                         ║ ║
║  │  │                                      │  ┌────╗                 ║ ║
║  │  │                                      │  │    ╚═════════════════╝ ║
║  │  │                                      │  │                        ║
║  │  │                                      │  │                        ║
║  │  │                 ╔════════════════════╝  ╚╗                       ║
║  │  └─────────────────╝ Hospital Reception     ║                       ║
║  │                                             ║                       ║
║  └────────────────────╗                        ║                       ║
║                       ║                        ║                       ║
║                       ║                        ║                       ║
║                       ║                        ║                       ║
║                       ╚══════════╗  ╔══════════╝                       ║
╚══════════════════════════════════╝  ╚══════════════════════════════════╝""")

    elif building == "Joe's House":
        print("""
╔══════════════════════════ JOE'S HOUSE - ROOMS ═════════════════════════╗
║                                                                        ║
║                                                                        ║
║                                                    ╔═════════════════╗ ║
║                                                    ║ Joe's Office    ║ ║
║                                              ┌─────╝                 ║ ║
║                                              │                       ║ ║
║                                              │  ┌──╗                 ║ ║
║                                              │  │  ║                 ║ ║
║                                              │  │  ╚═════════════════╝ ║
║                                              │  │                      ║
║                                              │  │                      ║
║                                             ╔╝  ╚════════════════════╗ ║
║                                             ║ Living Room            ║ ║
║                                             ║                        ║ ║
║                                             ║                        ║ ║
║                                             ║                        ║ ║
║                                             ║                        ║ ║
║                                             ║                        ║ ║
║                                             ╚══════════╗  ╔══════════╝ ║
╚════════════════════════════════════════════════════════╝  ╚════════════╝""")

    elif building == "Shipping Company":
        print("""
╔═══════════════════════ SHIPPING COMPANY - ROOMS ═══════════════════════╗
║ ╔════════════════════════════════════════════════════════════════════╗ ║
║ ║ Warehouse                                                          ║ ║
║ ║                                                                    ║ ║
║ ║                                                                    ║ ║
║ ║                                                                    ║ ║
║ ║                                                                    ║ ║
║ ║                                                                    ║ ║
║ ║                                                                    ║ ║
║ ║    ┌────────────                                                   ║ ║
║ ║    │ \ │││││││││                                                   ║ ║
║ ║    │──┌─────────                                                   ║ ║
║ ║   ╔╝  ╚════════════════════╗                                       ║ ║
║ ║   ║ Office                 ║                                       ║ ║
║ ║   ║                        ║                                       ║ ║
║ ║   ║                        ║                                       ║ ║
║ ║   ║                        ║                                       ║ ║
║ ║   ╚════════════════════════╝                                       ║ ║
║ ║                                                                    ║ ║
║ ╚══════════════════════════════════════════════════════╗  ╔══════════╝ ║
╚════════════════════════════════════════════════════════╝  ╚════════════╝""")


def print_map(current_room):
    if current_room["building"] != "Outside":
        print_building_map(current_room["building"])
    else:
        print_city_map(map_s.police_visible, map_s.hospital_visible, map_s.shipping_visible, map_s.victim_visible)