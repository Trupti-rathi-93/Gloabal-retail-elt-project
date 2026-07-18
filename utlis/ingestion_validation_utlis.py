from config.schema_config import EXPECTED_SCHEMA

class IngestionValidationUtlis:
    '''
    '''
    def __init__(self):
        pass

    def validate_schema(self, dataframe):
        '''
        Validate the schema of the ingested data.
        '''
        actual_schema = list(dataframe.columns)

        missing_columns = [col for col in EXPECTED_SCHEMA if col not in actual_schema]

        extra_columns = [col for col in actual_schema if col not in EXPECTED_SCHEMA]    

        if actual_schema == EXPECTED_SCHEMA:
            return {
                'is_valid': True,
                'error_message': None,
                'missing_columns': [],
                'extra_columns': []
            }
        else:
            return {
                'is_valid': False,
                'error_message': f"Schema mismatch",
                'missing_columns': missing_columns,
                'extra_columns': extra_columns
            }

