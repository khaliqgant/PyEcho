import PyEcho
# Listen for events.
# This is naïve, it assumes the above worked.
while True:
    # Fetch our tasks
    tasks = echo.tasks()

   # Process each one
    for task in tasks:
       # Do something depending on the task here.
        print "New task found: " + task['text']

      # Now that we're done with it, delete it.
      # Again, this is naïve. We should error check the response code.
        echo.deleteTask(task)

   # Wait 10 seconds and do it again
    time.sleep(10)