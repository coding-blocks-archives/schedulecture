# schedulecture
A lecture schdeuler (we have classes, batches, centres, lecture rooms and teachers - this is really needed)

## Technologies 
### Backend
 - Python
 - Django (handles relationships well)
 
### Frontend

We'll figure out if we need to make a webapp or static pages can cut the cake  
We need a good calendar-like UI to drag and drop lectures into. 


## Motivation
At **Coding Blocks** scheduling lectures is not an easy task. Here are the variable factors that we have. 

### Models 
#### 1. Centres
We have multiple physical centres like Pitampura, Dwarka etc.

##### 1.1 Lecture Halls
Each physical centre has many lecture hall (halls belong to a centre). They have different capacities.

#### 2. Courses
There are multiple courses, like C++, Java, Android etc. 

##### 2.1 Batches
Multiple batches of each course is formed. A batch is a single iteration of a course, at a particular centre. Example batches are - 
 - Pandora Pitampura 2017 Summer
 - Launchpad Dwarka 2017 Spring


Batches have a start and end date (the end date being flexible). They have a pre-defined number of classes, but it can vary by 2-3 classes (plus or minus). 


###### 2.1.1 Lecture
A class of a batch scheduled on a particular time is a lecture. For ex. the Pandora batch has 20 lectures, more or less.
It is the single indivisible unit we are operating on here. It is the lectures that we have to schedule. 
A lecture, to be scheduled, must have a start and end time defined.

#### 3. Teachers
The main component - the person who'll teach in a batch. 

### Constraints
 1. A teacher cannot be at two places at the same time. 
 2. We can only schedule a single lecture at a time in a lecture hall. Overlappings are not possible.
 3. A lecture can only be scheduled if the batch size is smaller than the capacity of the lecture hall.
 
