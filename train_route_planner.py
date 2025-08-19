class Station:
    def __init__(self, name):
        self.name = name
        self.next = None
        self.prev = None

class RoutePlanner:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_station(self, name):
        new_station = Station(name)
        if not self.head:
            self.head = self.tail = new_station
        else:
            self.tail.next = new_station
            new_station.prev = self.tail
            self.tail = new_station
        print(f"✅ Station '{name}' added.")

    def make_circular(self):
        if self.head and self.tail:
            self.tail.next = self.head
            self.head.prev = self.tail
            print("🔁 Circular route enabled.")

    def display_forward(self, count=10):
        print("\n🚄 Forward Route:")
        current = self.head
        visited = 0
        while current and visited < count:
            print(f"➡️ {current.name}")
            current = current.next
            visited += 1
        print()

    def display_backward(self, count=10):
        print("\n🚄 Backward Route:")
        current = self.tail
        visited = 0
        while current and visited < count:
            print(f"⬅️ {current.name}")
            current = current.prev
            visited += 1
        print()

# --- Demo for testing ---
if __name__ == "__main__":
    planner = RoutePlanner()

    # Add some stations
    planner.add_station("Station A")
    planner.add_station("Station B")
    planner.add_station("Station C")
    planner.add_station("Station D")

    # Display normal navigation
    planner.display_forward()
    planner.display_backward()

    # Convert to circular route
    planner.make_circular()

    # Simulate circular navigation
    print("🔁 Circular Navigation (Forward):")
    node = planner.head
    for _ in range(8):
        print(f"🚉 {node.name}")
        node = node.next

    print("\n🔁 Circular Navigation (Backward):")
    node = planner.tail
    for _ in range(8):
        print(f"🚉 {node.name}")
        node = node.prev