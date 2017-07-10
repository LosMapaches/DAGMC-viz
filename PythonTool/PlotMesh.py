from visit import *


def PlotMesh(File):
    # Mesh plot attributes.

    if File is not None:
        File = list(File)

        Attribute = MeshAttributes()

        Attribute.showInternal = 1

        for item in File:
            if item[1].title() == "Mesh":
                # Check for optional inputs in Dictionary input.
                try:
                    Attribute.lineStyle = eval(
                                               "Attribute." +
                                               str(item[3]).upper()
                                               )
                except Exception:
                    pass

        SetPlotOptions(Attribute)