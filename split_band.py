from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
from qgis.core import QgsProcessingParameterRasterLayer
from qgis.core import QgsProcessingParameterRasterDestination
import processing


class Split_bands(QgsProcessingAlgorithm):

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterRasterLayer('inputimage', 'INPUT_IMAGE', defaultValue=None))
        self.addParameter(QgsProcessingParameterRasterDestination('R_conv', 'R_conv', createByDefault=True, defaultValue=None))
        self.addParameter(QgsProcessingParameterRasterDestination('G_conv', 'G_conv', createByDefault=True, defaultValue=None))
        self.addParameter(QgsProcessingParameterRasterDestination('B_conv', 'B_conv', createByDefault=True, defaultValue=None))
        self.addParameter(QgsProcessingParameterRasterDestination('Blue', 'BLUE', createByDefault=True, defaultValue=None))
        self.addParameter(QgsProcessingParameterRasterDestination('Green', 'GREEN', createByDefault=True, defaultValue=None))
        self.addParameter(QgsProcessingParameterRasterDestination('Red', 'RED', createByDefault=True, defaultValue=None))

    def processAlgorithm(self, parameters, context, model_feedback):
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        feedback = QgsProcessingMultiStepFeedback(4, model_feedback)
        results = {}
        outputs = {}

        # Split RGB bands
        alg_params = {
            'INPUT': parameters['inputimage'],
            'B': parameters['Blue'],
            'G': parameters['Green'],
            'R': parameters['Red']
        }
        outputs['SplitRgbBands'] = processing.run('saga:splitrgbbands', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Blue'] = outputs['SplitRgbBands']['B']
        results['Green'] = outputs['SplitRgbBands']['G']
        results['Red'] = outputs['SplitRgbBands']['R']

        feedback.setCurrentStep(1)
        if feedback.isCanceled():
            return {}

        # Translate (convert format)
        alg_params = {
            'COPY_SUBDATASETS': False,
            'DATA_TYPE': 0,
            'INPUT': outputs['SplitRgbBands']['R'],
            'NODATA': None,
            'OPTIONS': '',
            'TARGET_CRS': parameters['inputimage'],
            'OUTPUT': parameters['R_conv']
        }
        outputs['TranslateConvertFormat'] = processing.run('gdal:translate', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['R_conv'] = outputs['TranslateConvertFormat']['OUTPUT']

        feedback.setCurrentStep(2)
        if feedback.isCanceled():
            return {}

        # Translate (convert format)
        alg_params = {
            'COPY_SUBDATASETS': False,
            'DATA_TYPE': 0,
            'INPUT': outputs['SplitRgbBands']['B'],
            'NODATA': None,
            'OPTIONS': '',
            'TARGET_CRS': parameters['inputimage'],
            'OUTPUT': parameters['B_conv']
        }
        outputs['TranslateConvertFormat'] = processing.run('gdal:translate', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['B_conv'] = outputs['TranslateConvertFormat']['OUTPUT']

        feedback.setCurrentStep(3)
        if feedback.isCanceled():
            return {}

        # Translate (convert format)
        alg_params = {
            'COPY_SUBDATASETS': False,
            'DATA_TYPE': 0,
            'INPUT': outputs['SplitRgbBands']['G'],
            'NODATA': None,
            'OPTIONS': '',
            'TARGET_CRS': parameters['inputimage'],
            'OUTPUT': parameters['G_conv']
        }
        outputs['TranslateConvertFormat'] = processing.run('gdal:translate', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['G_conv'] = outputs['TranslateConvertFormat']['OUTPUT']
        return results

    def name(self):
        return 'Split_bands'

    def displayName(self):
        return 'Split_bands'

    def group(self):
        return ''

    def groupId(self):
        return ''

    def createInstance(self):
        return Split_bands()
