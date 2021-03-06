class Project():
    """The raster data and annotations associated with an area of interest."""

    def __init__(self, raster_source=None,
                ground_truth_annotation_source=None,
                prediction_annotation_source=None):
        """Construct a new Project.

        Args:
            raster_source: optional RasterSource
            ground_truth_annotation_source: optional AnnotationSource
            prediction_annotation_source: optional AnnotationSource
        """
        self.raster_source = raster_source
        self.ground_truth_annotation_source = ground_truth_annotation_source
        self.prediction_annotation_source = prediction_annotation_source
