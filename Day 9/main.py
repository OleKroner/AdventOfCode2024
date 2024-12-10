import sys

disk = []
disk_defragmented = []

def display_progress(current, total, prefix="Progress", length=50):
    """Displays a simple progress bar."""
    percent = f"{100 * (current / total):.1f}"
    filled_length = int(length * current // total)
    bar = "█" * filled_length + "-" * (length - filled_length)
    sys.stdout.write(f"\r{prefix}: |{bar}| {percent}% Complete")
    sys.stdout.flush()
    if current == total:
        sys.stdout.write("\n")

with open("./input.txt") as file:
    for id, size in enumerate(file.read()):
        if id % 2 == 0:
            for i in range(int(size)):
                disk.append(id // 2)
            disk_defragmented.append((id // 2, int(size)))
            continue
        for i in range(int(size)):
            disk.append(".")
            disk_defragmented.append(".")

is_not_complete = True
last_position = 1

free_disk_space = disk.count(".")

items_processed = 0
while is_not_complete:
    for i in range(last_position, len(disk) + 1):
        item = disk[-i]

        if item == ".":
            items_processed += 1
            display_progress(items_processed, free_disk_space, "Compacting Disk")
            continue

        swap_position = disk.index(".")
        if len(disk) - i - 1 > swap_position:
            del disk[swap_position]
            disk.insert(swap_position, item)
            del disk[-i]
            disk.append(".")
            last_position = i
            break
        else:
            is_not_complete = False
            break

checksum = 0

for index, id in enumerate(disk):
    if id == ".": break
    checksum += index * id

disk_length = len(disk_defragmented)

last_position = 1

items_processed = 0
for i in range(last_position, len(disk_defragmented) + 1):
    items_processed += 1
    display_progress(items_processed, disk_length, "Compacting Disk (new method)")
    item = disk_defragmented[-i]

    if item == ".":
        continue

    swap_position = disk_defragmented.index(".")
    while len(disk_defragmented) - i - 1 > swap_position:
        if disk_defragmented[swap_position:swap_position + item[1]].count(".") == item[1]:
            del disk_defragmented[swap_position:swap_position + item[1]]
            disk_defragmented.insert(swap_position, item)
            for x in range(item[1]):
                disk_defragmented.insert(-i, ".")
            del disk_defragmented[-i]
            break
        if swap_position + item[1] - 1 >= disk_length: break
        try:
            swap_position = disk_defragmented.index(".", swap_position + 1)
        except ValueError:
            break
            
        last_position = i

defragmented_disk = []

for file in disk_defragmented:
    if file == ".":
        defragmented_disk.append(".")
        continue
    for i in range(file[1]):
        defragmented_disk.append(file[0])

checksum_defragented = 0

for index, id in enumerate(defragmented_disk):
    if id == ".": continue
    checksum_defragented += index * id

print("Checksum first-method:", checksum)
print("Checksum new-method:", checksum_defragented)