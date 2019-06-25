from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
from qgis.core import QgsProcessingParameterRasterLayer
from qgis.core import QgsProcessingParameterRasterDestination
import processing


class Calculate_ndvi(QgsProcessingAlgorithm):

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterRasterLayer('inputnirband', 'INPUT_NIR_BAND', defaultValue=None))
        self.addParameter(QgsProcessingParameterRasterLayer('inputredband', 'INPUT_RED_BAND', defaultValue=None))
        self.addParameter(QgsProcessingParameterRasterDestination('Output', 'OUTPUT', createByDefault=True, defaultValue=None))

    def processAlgorithm(self, parameters, context, model_feedback):
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        feedback = QgsProcessingMultiStepFeedback(1, model_feedback)
        results = {}
        outputs = {}

        # Raster calculator
        alg_params = {
            'CELLSIZE': 0.03,
            'CRS': parameters['inputnirband'],
            'EXPRESSION': ' ( \"INPUT_NIR_BAND@1\" - \"INPUT_RED_BAND@1\" )  /  ( \"INPUT_NIR_BAND@1\" + \"INPUT_RED_BAND@1\" ) ',
            'EXTENT': parameters['inputnirband'],
            'LAYERS': [],
            'OUTPUT': parameters['Output']
        }
        outputs['RasterCalculator'] = processing.run('qgis:rastercalculator', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Output'] = outputs['RasterCalculator']['OUTPUT']
        return results

    def name(self):
        return 'Calculate_NDVI'

    def displayName(self):
        return 'Calculate_NDVI'

    def group(self):
        return 'AWF'

    def groupId(self):
        return 'AWF'

    def createInstance(self):
        return Calculate_ndvi()
