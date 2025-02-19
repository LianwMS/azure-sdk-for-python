# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: sample_train_model_with_labels.py

DESCRIPTION:
    This sample demonstrates how to train a model with labels. For this sample, you can use the training
    forms found in https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/formrecognizer/azure-ai-formrecognizer/samples/sample_forms/training
    Upload the forms to your storage container and then generate a container SAS URL using these instructions:
    https://docs.microsoft.com/azure/cognitive-services/form-recognizer/quickstarts/python-labeled-data#train-a-model-using-labeled-data

    To see how to label your documents, you can use the service's labeling tool to label your documents:
    https://docs.microsoft.com/azure/cognitive-services/form-recognizer/quickstarts/label-tool. Follow the
    instructions to store these labeled files in your blob container with the other form files.
    See sample_recognize_custom_forms.py to recognize forms with your custom model.

USAGE:
    python sample_train_model_with_labels.py

    Set the environment variables with your own values before running the sample:
    1) AZURE_FORM_RECOGNIZER_ENDPOINT - the endpoint to your Cognitive Services resource.
    2) AZURE_FORM_RECOGNIZER_KEY - your Form Recognizer API key
    3) CONTAINER_SAS_URL - The shared access signature (SAS) Url of your Azure Blob Storage container with your labeled data.
        See https://docs.microsoft.com/azure/cognitive-services/form-recognizer/quickstarts/python-labeled-data#train-a-model-using-labeled-data
        for more detailed descriptions on how to get it.
"""

import os


class TrainModelWithLabelsSample(object):

    def train_model_with_labels(self):
        from azure.ai.formrecognizer import FormTrainingClient
        from azure.core.credentials import AzureKeyCredential

        endpoint = os.environ["AZURE_FORM_RECOGNIZER_ENDPOINT"]
        key = os.environ["AZURE_FORM_RECOGNIZER_KEY"]
        container_sas_url = os.environ["CONTAINER_SAS_URL"]

        form_training_client = FormTrainingClient(endpoint, AzureKeyCredential(key))
        poller = form_training_client.begin_training(container_sas_url, use_training_labels=True)
        model = poller.result()

        # Custom model information
        print("Model ID: {}".format(model.model_id))
        print("Status: {}".format(model.status))
        print("Training started on: {}".format(model.training_started_on))
        print("Training completed on: {}".format(model.training_completed_on))

        print("Recognized fields:")
        # looping through the submodels, which contains the fields they were trained on
        # The labels are based on the ones you gave the training document.
        for submodel in model.submodels:
            print("...The submodel with form type {} has accuracy '{}'".format(submodel.form_type, submodel.accuracy))
            for name, field in submodel.fields.items():
                print("...The model found field '{}' to have name '{}' with an accuracy of {}".format(
                    name, field.name, field.accuracy
                ))

        # Training result information
        for doc in model.training_documents:
            print("Document name: {}".format(doc.document_name))
            print("Document status: {}".format(doc.status))
            print("Document page count: {}".format(doc.page_count))
            print("Document errors: {}".format(doc.errors))


if __name__ == '__main__':
    sample = TrainModelWithLabelsSample()
    sample.train_model_with_labels()
