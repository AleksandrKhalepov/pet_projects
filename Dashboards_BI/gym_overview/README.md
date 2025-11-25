## Training Dashboard
This is pet project based on my training journey in a gym. Not so far ago I have started working out, so I decided that it will be an excellent idea to combine my daily life routine with my job. 

# Task definition
My main goal was to create dashboard, which will answer many common questions about my training. I also want to have an overview of my program, some insights etc.
In fact, I sketched my viz even before I actually collected the data (this is game changing experience, because after collection I can adjust my sketch for improving my final viz).


Collected data in google sheets looks like this:

  book1 - sessions:
  
      session_id - unique id of a session
      
      start - session time start
      
      end - session end time
      
  book2 - workout_exercises
  
      session_id - unique id of a session
      
      exercise_name - name of the machine/exercise
      
      set_number - set number in chronological order between an exercise
      
      reps_number - number of repetitions in a set
      
      lb - weight in lb (most of the equipment is in a lb, so by default values are in it, if weight is in kg it will appear as  "__kg")

After data preparation I sketch some ideas of dashboard layout and begin work

## Dashboard
(https://public.tableau.com/views/Workoutsummary/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

# Overall results

Am I satisfied with a final result?
Yes, something about 8/10

What did I succeed at?

Viz is capable of decent overview and revealing trends in my workout.
For instance, if I get asked, how much sets I do more often 2 of 3, I don`t need to desperately count in my head, sometimes in is almost impossible to predict empirically. 


Clarity. I know how much time my workout takes on average, I know most of my training patterns, so I can easily adjust program for my needs.

What I could not handle?

I suppose, the project should have had clearer requirements, as I was feeling a bit lost around the end, because I wanted to add something to a viz. Also in this exact project I was trying to implement as many things as possible in Tableau itself, but in reality it was horrible idea and all the calculations would be much more optimal in a sheet or database. This is why I am in love with Superset)

P.S.: Unfortunately, Tableau Public does not allow to automatically update data, so I decided to end project on 17-ish sessions. This is pretty much enough for semi-decent analysis. If you have any comments about this project, please be welcome to give feedback (aleksandr_khalepov@mail.ru). Thanks a lot.
