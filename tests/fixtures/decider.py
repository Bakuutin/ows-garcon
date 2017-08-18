history = {'events': [
    {'eventId': 1,
     'eventTimestamp': 1419350960.696,
     'eventType': 'WorkflowExecutionStarted',
     'workflowExecutionStartedEventAttributes': {
         'childPolicy': 'TERMINATE',
         'executionStartToCloseTimeout': '3600',
         'parentInitiatedEventId': 0,
         'taskList': {'name': 'garcon_decider'},
         'taskStartToCloseTimeout': '300',
         'workflowType': {'name': 'garcon_decider', 'version': '1.0'}}},
    {'decisionTaskScheduledEventAttributes': {
        'startToCloseTimeout': '300',
        'taskList': {'name': 'garcon_decider'}},
     'eventId': 2,
     'eventTimestamp': 1419350960.696,
     'eventType': 'DecisionTaskScheduled'},
    {'decisionTaskStartedEventAttributes': {
        'scheduledEventId': 2},
     'eventId': 3,
     'eventTimestamp': 1419350960.767,
     'eventType': 'DecisionTaskStarted'},
    {'decisionTaskCompletedEventAttributes': {
        'scheduledEventId': 2, 'startedEventId': 3},
     'eventId': 4,
     'eventTimestamp': 1419350960.945,
     'eventType': 'DecisionTaskCompleted'},
    {'activityTaskScheduledEventAttributes': {
        'activityId': 'workflow_name_activity_1-1',
        'activityType': {'name': 'workflow_name_activity_1', 'version': '1.0'},
        'decisionTaskCompletedEventId': 4,
        'heartbeatTimeout': '600',
        'input': 'json object',
        'scheduleToCloseTimeout': '3900',
        'scheduleToStartTimeout': '300',
        'startToCloseTimeout': '3600',
        'taskList': {'name': 'garcon_workflow_name_activity_1'}},
     'eventId': 5,
     'eventTimestamp': 1419350960.945,
     'eventType': 'ActivityTaskScheduled'},
    {'activityTaskStartedEventAttributes': {
        'scheduledEventId': 5},
     'eventId': 6,
     'eventTimestamp': 1419351025.473,
     'eventType': 'ActivityTaskStarted'},
    {'activityTaskCompletedEventAttributes': {
        'scheduledEventId': 5, 'startedEventId': 6},
     'eventId': 7,
     'eventTimestamp': 1419351025.534,
     'eventType': 'ActivityTaskCompleted'},
    {'decisionTaskScheduledEventAttributes': {
        'startToCloseTimeout': '300',
        'taskList': {'name': 'garcon_decider'}},
     'eventId': 8,
     'eventTimestamp': 1419351025.534,
     'eventType': 'DecisionTaskScheduled'},
    {'decisionTaskStartedEventAttributes': {'scheduledEventId': 8},
     'eventId': 9,
     'eventTimestamp': 1419351026.066,
     'eventType': 'DecisionTaskStarted'},
    {'decisionTaskCompletedEventAttributes': {
        'scheduledEventId': 8, 'startedEventId': 9},
     'eventId': 10,
     'eventTimestamp': 1419351026.232,
     'eventType': 'DecisionTaskCompleted'},
    {'activityTaskScheduledEventAttributes': {
        'activityId': 'workflow_name_activity_2-1',
        'activityType': {'name': 'workflow_name_activity_2', 'version': '1.0'},
        'decisionTaskCompletedEventId': 10,
        'heartbeatTimeout': '600',
        'input': 'json object',
        'scheduleToCloseTimeout': '3900',
        'scheduleToStartTimeout': '300',
        'startToCloseTimeout': '3600',
        'taskList': {'name': 'garcon_workflow_name_activity_2'}},
     'eventId': 11,
     'eventTimestamp': 1419351026.232,
     'eventType': 'ActivityTaskScheduled'},
    {'activityTaskScheduledEventAttributes': {
        'activityId': 'workflow_name_activity_3-1',
        'activityType': {'name': 'workflow_name_activity_3', 'version': '1.0'},
        'decisionTaskCompletedEventId': 10,
        'heartbeatTimeout': '600',
        'input': 'json object',
        'scheduleToCloseTimeout': '3900',
        'scheduleToStartTimeout': '300',
        'startToCloseTimeout': '3600',
        'taskList': {'name': 'garcon_workflow_name_activity_3'}},
     'eventId': 12,
     'eventTimestamp': 1419351026.232,
     'eventType': 'ActivityTaskScheduled'},
    {'activityTaskStartedEventAttributes': {
        'scheduledEventId': 12},
     'eventId': 13,
     'eventTimestamp': 1419351026.357,
     'eventType': 'ActivityTaskStarted'},
    {'activityTaskCompletedEventAttributes': {
        'scheduledEventId': 12, 'startedEventId': 13},
     'eventId': 14,
     'eventTimestamp': 1419351026.437,
     'eventType': 'ActivityTaskCompleted'},
    {'decisionTaskScheduledEventAttributes': {
        'startToCloseTimeout': '300',
        'taskList': {'name': 'garcon_decider'}},
     'eventId': 15,
     'eventTimestamp': 1419351026.437,
     'eventType': 'DecisionTaskScheduled'},
    {'activityTaskStartedEventAttributes': {
        'scheduledEventId': 11},
     'eventId': 16,
     'eventTimestamp': 1419351026.542,
     'eventType': 'ActivityTaskStarted'},
    {'decisionTaskStartedEventAttributes': {
        'scheduledEventId': 15},
     'eventId': 17,
     'eventTimestamp': 1419351026.622,
     'eventType': 'DecisionTaskStarted'},
    {'decisionTaskCompletedEventAttributes': {
        'scheduledEventId': 15, 'startedEventId': 17},
     'eventId': 18,
     'eventTimestamp': 1419351026.803,
     'eventType': 'DecisionTaskCompleted'},
    {'activityTaskCompletedEventAttributes': {
        'scheduledEventId': 11, 'startedEventId': 16},
     'eventId': 19,
     'eventTimestamp': 1419351026.932,
     'eventType': 'ActivityTaskCompleted'},
    {'decisionTaskScheduledEventAttributes': {
        'startToCloseTimeout': '300',
        'taskList': {'name': 'garcon_decider'}},
     'eventId': 20,
     'eventTimestamp': 1419351026.932,
     'eventType': 'DecisionTaskScheduled'},
    {'decisionTaskStartedEventAttributes': {'scheduledEventId': 20},
     'eventId': 21,
     'eventTimestamp': 1419351027.276,
     'eventType': 'DecisionTaskStarted'},
    {'decisionTaskCompletedEventAttributes': {
        'scheduledEventId': 20, 'startedEventId': 21},
     'eventId': 22,
     'eventTimestamp': 1419351027.381,
     'eventType': 'DecisionTaskCompleted'},
    {'activityTaskScheduledEventAttributes': {
        'activityId': 'workflow_name_activity_4-1',
        'activityType': {'name': 'workflow_name_activity_4', 'version': '1.0'},
        'decisionTaskCompletedEventId': 22,
        'heartbeatTimeout': '600',
        'input': 'json object',
        'scheduleToCloseTimeout': '3900',
        'scheduleToStartTimeout': '300',
        'startToCloseTimeout': '3600',
        'taskList': {'name': 'garcon_workflow_name_activity_4'}},
     'eventId': 23,
     'eventTimestamp': 1419351027.381,
     'eventType': 'ActivityTaskScheduled'},
    {'activityTaskStartedEventAttributes': {'scheduledEventId': 23},
     'eventId': 24,
     'eventTimestamp': 1419351027.43,
     'eventType': 'ActivityTaskStarted'},
    {'activityTaskCompletedEventAttributes': {
        'scheduledEventId': 23, 'startedEventId': 24},
     'eventId': 25,
     'eventTimestamp': 1419351027.492,
     'eventType': 'ActivityTaskCompleted'},
    {'decisionTaskScheduledEventAttributes': {
        'startToCloseTimeout': '300',
        'taskList': {'name': 'garcon_decider'}},
     'eventId': 26,
     'eventTimestamp': 1419351027.492,
     'eventType': 'DecisionTaskScheduled'},
    {'decisionTaskStartedEventAttributes': {'scheduledEventId': 26},
     'eventId': 27,
     'eventTimestamp': 1419351027.555,
     'eventType': 'DecisionTaskStarted'}],
    'workflowExecution': {
    'runId': '123abc=',
    'workflowId': 'test-workflow-id'}
}
