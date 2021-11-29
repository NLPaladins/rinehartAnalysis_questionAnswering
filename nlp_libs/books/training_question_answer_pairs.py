def filter_mega_string(mega_string): 
    return ' '.join(list(filter(lambda x: len(x) > 0, mega_string.replace('\n', ' ').split(' '))))

def create_question_object(context, questions, answers): 
    return {
        "context": context,
        "questions": questions,
        "answers": answers
    }


    ########################################################
    #######################Proagonist#########################
    ########################################################
protagonist_arrival = filter_mega_string("""At ten o'clock the Casanova hack brought up three men. They introduced
themselves as the coroner of the county and two detectives from the
city. The coroner led the way at once to the locked wing, and with the
aid of one of the detectives examined the rooms and the body. The other
detective, after a short scrutiny of the dead man, busied himself with
the outside of the house. It was only after they had got a fair idea of
things as they were that they sent for me.


I received them in the living-room, and I had made up my mind exactly
what to tell. I had taken the house for the summer, I said, while the
Armstrongs were in California. In spite of a rumor among the servants
about strange noises-I cited Thomas-nothing had occurred the first two
nights. On the third night I believed that some one had been in the
house: I had heard a crashing sound, but being alone with one maid had
not investigated. The house had been locked in the morning and
apparently undisturbed.

Then, as clearly as I could, I related how, the night before, a shot
had roused us; that my niece and I had investigated and found a body;
that I did not know who the murdered man was until Mr. Jarvis from the
club informed me, and that I knew of no reason why Mr. Arnold Armstrong
should steal into his father's house at night. I should have been glad
to allow him entree there at any time.

"Have you reason to believe, Miss Innes," the coroner asked, "that any
member of your household, imagining Mr. Armstrong was a burglar, shot
him in self-defense?"

"I have no reason for thinking so," I said quietly.

"Your theory is that Mr. Armstrong was followed here by some enemy, and
shot as he entered the house?"

"I don't think I have a theory," I said. "The thing that has puzzled me
is why Mr. Armstrong should enter his father's house two nights in
succession, stealing in like a thief, when he needed only to ask
entrance to be admitted."
""")

protagonist_arrival_questions = [
    "When did the detectives arrive?",
    "What did the coroner do?",
    "Where were the detectives received?",
    "How did Mr. Armstrong die?",
    "Who informed Miss Innes about the murder?",
    "Where were the Armstrongs during Summer?",
]

protagonist_arrival_answers = [
    {"text": "ten o'clock", "answer_start":3 },
    {"text": "examined the rooms and the body", "answer_start":239 },
    {"text": "in the living-room", "answer_start":484 },
    {"text": "shot", "answer_start":1039 },
    {"text": "Mr. Jarvis", "answer_start":1165 },
    {"text": "in California", "answer_start":624 }
]

    ########################################################
    #######################Antagonists#########################
    ########################################################

antagonist_arrival = filter_mega_string("""
Once in the drawing-room, Gertrude collapsed and went from one fainting
spell into another. I had all I could do to keep Liddy from drowning
her with cold water, and the maids huddled in a corner, as much use as
so many sheep. In a short time, although it seemed hours, a car came
rushing up, and Anne Watson, who had waited to dress, opened the door.
Three men from the Greenwood Club, in all kinds of costumes, hurried
in. I recognized a Mr. Jarvis, but the others were strangers.

"What's wrong?" the Jarvis man asked-and we made a strange picture, no
doubt. "Nobody hurt, is there?" He was looking at Gertrude.

"Worse than that, Mr. Jarvis," I said. "I think it is murder."

At the word there was a commotion. The cook began to cry, and Mrs.
Watson knocked over a chair. The men were visibly impressed.


"Not any member of the family?" Mr. Jarvis asked, when he had got his
breath.

"No," I said; and motioning Liddy to look after Gertrude, I led the way
with a lamp to the card-room door. One of the men gave an exclamation,
and they all hurried across the room. Mr. Jarvis took the lamp from
me-I remember that-and then, feeling myself getting dizzy and
light-headed, I closed my eyes. When I opened them their brief
examination was over, and Mr. Jarvis was trying to put me in a chair.

"You must get up-stairs," he said firmly, "you and Miss Gertrude, too.
This has been a terrible shock. In his own home, too."

I stared at him without comprehension. "Who is it?" I asked with
difficulty. There was a band drawn tight around my throat.

"It is Arnold Armstrong," he said, looking at me oddly, "and he has
been murdered in his father's house."

After a minute I gathered myself together and Mr. Jarvis helped me into
the living-room. Liddy had got Gertrude up-stairs, and the two strange
men from the club stayed with the body. The reaction from the shock and
strain was tremendous: I was collapsed-and then Mr. Jarvis asked me a
question that brought back my wandering faculties.
""")


antagonist_arrival_questions = [
    "Who fainted?",
    "What's wrong?",
    "Why did Mrs. Watston knock over a chair?",
    "Who opened the door?",
    "Where did Mr. Jarvis come from?",
    "How Many people came to help?",
    "Who helped Gertrude?"
]

antagonist_arrival_answers = [
    {"text": "Gertrude", "answer_start": 26},
    {"text": "murder", "answer_start": 668},
    {"text": "murder", "answer_start": 668},
    {"text": "Anne Watson", "answer_start": 297},
    {"text": "the Greenwood Club", "answer_start": 367},
    {"text": "Three", "answer_start": 352}, 
    {"text": "Liddy", "answer_start": 121}
]

########################################################
#######################  Crime Scenes #########################
########################################################

crime_scene_context = filter_mega_string("""
At three o'clock in the morning I was roused by a revolver shot. The
sound seemed to come from just outside my door. For a moment I could
not move. Then-I heard Gertrude stirring in her room, and the next
moment she had thrown open the connecting door.

"O Aunt Ray! Aunt Ray!" she cried hysterically. "Some one has been
killed, killed!"

"Thieves," I said shortly. "Thank goodness, there are some men in the
house to-night." I was getting into my slippers and a bath-robe, and
Gertrude with shaking hands was lighting a lamp. Then we opened the
door into the hall, where, crowded on the upper landing of the stairs,
the maids, white-faced and trembling, were peering down, headed by
Liddy. I was greeted by a series of low screams and questions, and I
tried to quiet them.

Gertrude had dropped on a chair and sat there limp and shivering.

I went at once across the hall to Halsey's room and knocked; then I
pushed the door open. It was empty; the bed had not been occupied!

"He must be in Mr. Bailey's room," I said excitedly, and followed by
Liddy, we went there. Like Halsey's, it had not been occupied! Gertrude
was on her feet now, but she leaned against the door for support.

"They have been killed!" she gasped. Then she caught me by the arm and
dragged me toward the stairs. "They may only be hurt, and we must find
them," she said, her eyes dilated with excitement.

I don't remember how we got down the stairs: I do remember expecting
every moment to be killed. The cook was at the telephone up-stairs,
calling the Greenwood Club, and Liddy was behind me, afraid to come and
not daring to stay behind. We found the living-room and the
drawing-room undisturbed. Somehow I felt that whatever we found would
be in the card-room or on the staircase, and nothing but the fear that
Halsey was in danger drove me on; with every step my knees seemed to
give way under me. Gertrude was ahead and in the card-room she stopped,
holding her candle high. Then she pointed silently to the doorway into
the hall beyond. Huddled there on the floor, face down, with his arms
extended, was a man.

Gertrude ran forward with a gasping sob. "Jack," she cried, "oh, Jack!"

Liddy had run, screaming, and the two of us were there alone. It was
Gertrude who turned him over, finally, until we could see his white
face, and then she drew a deep breath and dropped limply to her knees.
It was the body of a man, a gentleman, in a dinner coat and white
waistcoat, stained now with blood-the body of a man I had never seen
before.
""")


crime_scene_questions = [
    "When the did the revolver shoot?", 
    "Where was Gertrude?", 
    "Was Halsey in his room?", 
    "Who was the cook calling?", 
    "Where was the man huddled?", 
    # "Which rooms did they check?", 
    "Did they find anyone in Mr. Bailey's room?", 
]

crime_scene_answers = [
    {"text": "three o'clock in the morning", "answer_start": 3},
    {"text": "in her room", "answer_start": 179},
    {"text": "It was empty; the bed had not been occupied!", "answer_start": 929},
    {"text": "the Greenwood Club", "answer_start": 1519},
    {"text": "on the floor, face down, with his arms extended", "answer_start": 2027},
    # {"text": "Three", "answer_start": 352},
    {"text": "it had not been occupied", "answer_start": 1080}
]

########################################################
#######################Evidence#########################
########################################################

evidence_context = filter_mega_string("""
"Sit down," he said, pushing forward a chair. "There are some things I
have to tell you, and, in return, please tell me all you know. Believe
me, things always come out. In the first place, Mr. Armstrong was shot
from above. The bullet was fired at close range, entered below the
shoulder and came out, after passing through the heart, well down the
back. In other words, I believe the murderer stood on the stairs and
fired down. In the second place, I found on the edge of the
billiard-table a charred cigar which had burned itself partly out, and
a cigarette which had consumed itself to the cork tip. Neither one had
been more than lighted, then put down and forgotten. Have you any idea
what it was that made your nephew and Mr. Bailey leave their cigars and
their game, take out the automobile without calling the chauffeur, and
all this at-let me see-certainly before three o'clock in the morning?"

"I don't know," I said; "but depend on it, Mr. Jamieson, Halsey will be
back himself to explain everything."

"I sincerely hope so," he said. "Miss Innes, has it occurred to you
that Mr. Bailey might know something of this?"

Gertrude had come down-stairs and just as he spoke she came in. I saw
her stop suddenly, as if she had been struck.

"He does not," she said in a tone that was not her own. "Mr. Bailey and
my brother know nothing of this. The murder was committed at three.
They left the house at a quarter before three."

"How do you know that?" Mr. Jamieson asked oddly. "Do you _know_ at
what time they left?"

"I do," Gertrude answered firmly. "At a quarter before three my brother
and Mr. Bailey left the house, by the main entrance. I-was-there."
""")


evidence_questions = [
    "From where was mister armstrong shot?",
    "How was the bullet fired?",
    "What was on the billiard-table?",
    "When did Halsey and Mr. Bailey take out the automobile?", 
    "When was the murder commmitted?", 
    "When did Halsey leave the house?", 
    "Who did Halsey leave with?"
]

evidence_answers = [
    {"text":  "from above", "answer_start": 213},
    {"text":  "at close range","answer_start": 246},
    {"text":  "a charred cigar", "answer_start": 494},
    {"text":  "certainly before three o'clock in the morning", "answer_start": 858},
    {"text":  "at three", "answer_start": 1376},
    {"text":  "At a quarter before three", "answer_start": 1559},
    {"text":  "Mr. Bailey","answer_start": 1600}
]


########################################################
#######################Resolution#########################
########################################################

resolution_context = filter_mega_string("""
On the way across the lawn she was confronted by Arnold, who for some
reason was determined to get into the house. He had a golf-stick in his
hand, that he had picked up somewhere, and on her refusal he had struck
her with it. One hand had been badly cut, and it was that, poisoning
having set in, which was killing her. She broke away in a frenzy of
rage and fear, and got into the house while Gertrude and Jack Bailey
were at the front door. She went up-stairs, hardly knowing what she was
doing. Gertrude's door was open, and Halsey's revolver lay there on the
bed. She picked it up and turning, ran part way down the circular
staircase. She could hear Arnold fumbling at the lock outside. She
slipped down quietly and opened the door: he was inside before she had
got back to the stairs. It was quite dark, but she could see his white
shirt-bosom. From the fourth step she fired. As he fell, somebody in
the billiard-room screamed and ran. When the alarm was raised, she had
had no time to get up-stairs: she hid in the west wing until every one
was down on the lower floor. Then she slipped upstairs, and threw the
revolver out of an upper window, going down again in time to admit the
men from the Greenwood Club.

If Thomas had suspected, he had never told. When she found the hand
Arnold had injured was growing worse, she gave the address of Lucien at
Richfield to the old man, and almost a hundred dollars. The money was
for Lucien's board until she recovered. She had sent for me to ask me
if I would try to interest the Armstrongs in the child. When she found
herself growing worse, she had written to Mrs. Armstrong, telling her
nothing but that Arnold's legitimate child was at Richfield, and
imploring her to recognize him. She was dying: the boy was an
Armstrong, and entitled to his father's share of the estate. The papers
were in her trunk at Sunnyside, with letters from the dead man that
would prove what she said. She was going; she would not be judged by
earthly laws; and somewhere else perhaps Lucy would plead for her. It
was she who had crept down the circular staircase, drawn by a magnet,
that night Mr. Jamieson had heard some one there. Pursued, she had fled
madly, anywhere-through the first door she came to. She had fallen down
the clothes chute, and been saved by the basket beneath. I could have
cried with relief; then it had not been Gertrude, after all!
""")


resolution_questions = [
    "How did Anne Watson get the gun?",
    "What did Anne Watson do with the gun?",
    "Where was Anne Watson confronted by Arnold?",
    "What did Arnold strike Anne Watson with?",
    "Where did the scream come from?",
    "To whom did the weapon belong?",
    "Who did they initially think was the murderer?"
]

resolution_answers = [
    {"text":  "Gertrude's door was open", "answer_start": 499},
    {"text":  "threw the revolver out of an upper window", "answer_start": 1110},
    {"text":  "On the way across the lawn", "answer_start": 0},
    {"text":  "golf-stick", "answer_start": 124},
    {"text":  "the billiard-room", "answer_start": 908},
    {"text":  "Halsey", "answer_start": 529},
    {"text":  "Gertrude", "answer_start": 2371}
]

#################################################
################ data objects ###################
#################################################

protagonist_data = create_question_object(
    protagonist_arrival, protagonist_arrival_questions, protagonist_arrival_answers
)
antagonist_data = create_question_object(
    antagonist_arrival, antagonist_arrival_questions, antagonist_arrival_answers
)
crime_scene_data = create_question_object(
    crime_scene_context, crime_scene_questions, crime_scene_answers
)
evidence_data = create_question_object(
    evidence_context, evidence_questions, evidence_answers
)
resolution_data = create_question_object(
    resolution_context, resolution_questions, resolution_answers
)

datalist = [
    protagonist_data,
    antagonist_data,
    crime_scene_data,
    evidence_data,
    resolution_data
]

total_contexts = []
total_questions = []
total_answers = []

for data in datalist:
    for index in range(len(data['questions'])):
        total_contexts.append(data['context'])
        total_questions.append(data['questions'][index])
        total_answers.append(data['answers'][index])
        if data['answers'][index]['text'] not in data['context']:
            print(data['context'])
            print(data['questions'][index])
            print(data['answers'][index]['text'])
            print("\n\n\n")

