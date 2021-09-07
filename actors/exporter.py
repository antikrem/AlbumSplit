from model.exportable_segment import ExportableSegment


class Exporter :

    def publish(self, exportableSegments: list[ExportableSegment]) :
        for publishedSegment in exportableSegments :
            publishedSegment.export(publishedSegment._name + ".mp3", "mp3")