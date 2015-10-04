#This script represents examples of a Reward() instance and a Task() instance 
#with the data already written.
#We stored the information into the django model from models.py
#In theory, the data would be inputed through the user's Google calendar and forms via the
#web application 



from core.models import Tasks,Rewards

# print Tasks.objects.all()
#REWARDS SECTION 
#format : [name, category, points, priority]
rewards = [["Go to Veggie Galaxy", "Eat", 20, "High"],["Go to a musical", "Performance", 80, "High"]]

a_reward = Rewards()

# not starting with [name, category, points, priority] list
for i in range(0,len(rewards)-1):
    a_reward.name += rewards[i][0]
    a_reward.category += rewards[i][1]
    a_reward.points += rewards[i][2]
    a_reward.priority += rewards[i][3]

print a_reward.name
print a_reward.category
print a_reward.points
print a_reward.priority

#TASKS SECTION
#format : ["name","category","points","due_date","difficulty"]
tasks = [["floss","hygiene",10,"everyday","easy"],["Write English paper","School","10/05","medium"]]

a_task = Tasks()

for i in range(0,len(tasks)-1):
    a_task.name += tasks[i][0]
    a_task.category += tasks[i][1]
    a_task.points += tasks[i][2]
    # a_task.due_date += tasks[i][3]
    a_task.difficulty += tasks[i][4]


print a_task.name
print a_task.category
print a_task.points
# print a_task.due_date
print a_task.difficulty

