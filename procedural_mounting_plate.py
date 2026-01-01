import cadquery as cq

def make_mounting_plate(
    width,
    height,
    thickness,
    hole_diameter,
    edge_offset_x,
    edge_offset_y,
):
    plate = (
        cq.Workplane("XY")
        .rect(width, height)
        .extrude(thickness)
    )

    hole_positions = [
        ( width/2 - edge_offset_x,  height/2 - edge_offset_y),
        (-width/2 + edge_offset_x,  height/2 - edge_offset_y),
        ( width/2 - edge_offset_x, -height/2 + edge_offset_y),
        (-width/2 + edge_offset_x, -height/2 + edge_offset_y),
    ]

    plate = (
        plate.faces(">Z")
        .workplane()
        .pushPoints(hole_positions)
        .hole(hole_diameter)
    )

    return plate


if __name__ == "__main__":
    plate = make_mounting_plate(
        width=100.0,
        height=60.0,
        thickness=5.0,
        hole_diameter=6.0,
        edge_offset_x=15.0,
        edge_offset_y=15.0,
    )

    cq.exporters.export(plate, "mounting_plate.step")
    print("Exported mounting_plate.step")
