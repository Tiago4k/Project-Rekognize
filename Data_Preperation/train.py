import turicreate as tc
tc.config.set_num_gpus(-1)

# Load the data
data = tc.SFrame('plate.sframe')

# Make a train-test split
train_data, test_data = data.random_split(0.8)

# Create a model
model = tc.object_detector.create(train_data)

# Save predictions to an SArray
predictions = model.predict(test_data)

# Evaluate the model and save the results into a dictionary
metrics = model.evaluate(test_data)

# Save the model for later use in Turi Create
model.save('model_plate_turi.model')

# Export for use in Core ML
model.export_coreml('model_plate_turi.mlmodel')
