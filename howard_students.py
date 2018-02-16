import random

# Let's assume we have a list of all of the Howard University students. Each
# element in the list is a 2-tuple (a tuple with 2 elements) containing the
# first name and the last name of a student.

# For example, a very short list would be:
# howard_students = [('John', 'Doe'), ('John', 'Dow'), ('Jane', 'Doe')]

# In practice, such a list would contain thousands of tuples considering
# the size of Howard University.

def print_FirstNames(students):
  fname = ''
  for x in students:
    student = students[students.index(x)]
    fname = student[0]
    print(fname.capitalize())
    
  # FIXME: write loop that prints all the first names (if two students
  # share the same first name you should print the first name twice).
  pass


def print_unique_first_names(students):
  b = 0
  uni_fname=set('')
  for g in students:
    student = students[students.index(g)]
    uni_fname.add(student[0])
    b += 1
  p = ', '.join(uni_fname)
  print(p)
    # FIXME: write loop that prints all the unique first names (if two
    # students share the same first name you should print the first name
    # only once).
    # Hint: what data structure could you use? dict. How many loops do you need?
  pass

def print_how_many_of_each_letter_we_need(students):
  y = 0
  dictn={}
  for _ in students:
    student= students[y]
    fullname= student[0].capitalize() + student[1].capitalize()
    
    for letter in fullname:
        dictn[letter] = 0
    for letter in fullname:
        dictn[letter] += 1
    y+=1
  print(dictn)

    # FIXME: write loop that prints how many of each letter in the alphabet
    # we need. For example, imagine we need to order t-shirts for every
    # student, and each t-shirt will have the student's full name in the back.
    # The cost of the t-shirt may depend on how many letters we need to
    # print, and each letter may have a different cost. For example, the
    # letter W (upper case) could cost more to print than the lower-case
    # letter o.
    # Hint: what data structure could you use? How many loops do you need?
  pass
  
def name_generator(num_syllables):
  syllables = ['la','em','ja','mu','to','ba','za','haka','tulu','xina','yefu','emo']
  #num_syllables = random.randint(1,25)
  name = ''
  for _ in range(num_syllables):
    name += syllables[random.randint(1,len(syllables)-1)]
  return name
    
def generate_random_student(first_names, last_names):
    first_name_index = random.randint(1, 9)
    first_names = name_generator(first_name_index)

    last_name_index = random.randint(1, 9)
    last_names = name_generator(last_name_index)

    return (first_names, last_names)

def generate_students_list(number_of_students):
    # FIXME: Build longer lists of possible first and last names. The names
    # don't really have to exist.
    # Hint: use the random number generator and a list of syllables to
    # generate names.
    
    #IMPLEMENT NAME_GENERATOR TO ADD TO THE FIRST AND LAST NAME LISTS BELOW TO INCREASE COMBINATIONS
    
    first_names = ['John', 'Jane', 'Bob']
    last_names = ['Doe', 'Dow', 'Daw']

    return [generate_random_student(first_names, last_names) for _ in range(number_of_students)]

# Let's test that code now...
# First, generate a list of (fake) students.

num_students = 110
random_students = generate_students_list(num_students)
if random_students is not None:
    assert len(random_students) == num_students
    howard_students = random_students
print('\n\t All first names:')
print_FirstNames(howard_students)

print('\n \t Unique first names:')
print_unique_first_names(howard_students)

print('\n\t How many of each letter we need:')
print_how_many_of_each_letter_we_need(howard_students)




