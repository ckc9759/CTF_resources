import anvil

region = anvil.Region.from_file("r.0.-1.mca")

for x in range(32):
    for z in range(32):
        try:
            chunk = anvil.Chunk.from_region(region, x, z)
            for te in chunk.tile_entities:
                if str(te["id"]) == "minecraft:chest":
                    if "LootTable" not in te:
                        items = te["Items"]
                        for item in items:
                            if "tag" in item:
                                if "Nope, not in this chest" not in item["tag"]["display"]["Name"]:
                                    print(item["tag"]["display"]["Name"])
                else:
                    continue
        except anvil.errors.ChunkNotFound as e:
            continue
