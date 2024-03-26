def task_asynchronous():
    while True:
        data = yield
        print("Receive:", data)
        # Treat data in asychrone way
        resultat = data * 2
        # Send the result
        yield resultat

# Create a generator object
task = task_asynchronous()
# Start the generator
next(task)

#send data to generator
resultat = task.send(10)
print("Result:", resultat)
