# 🎈 Elevator Pitch Chatbot

Elevator Pitch Chatbot is our team project of HackerNYU2025. Give us your project story and we will give you a great introduction product video!

## Inspiration

A lot of engineers are shy to pitch. Not to mention with our multicultural community here at USA, many are not native English speaker. We may have great ideas /great projects, but nervous and language barriers may recede success rate of getting invest by VC. Or  maybe reduce winning rate of this Hackathon!

## What it does

This is the website version of our project. You simply put in details of your idea, agent will generate you an elevator pitch, EVEN a Pitch Video Advertisement with realistic human Voice!

## Our Pitch (generated by our agent)
Are you an engineer with a great idea but struggle to pitch it confidently due to shyness or language barriers? Introducing our solution - a website where you can input your idea details and receive a professionally crafted elevator pitch or even a pitch video advertisement with voiceover! With our tool, you can effectively communicate your ideas to potential investors or judges at hackathons, increasing your chances of success. Don't let nervousness or language barriers hold you back from achieving your goals. Try our platform today and start pitching with confidence!

## How we built it

We utilized LLM and VLM based on ChatGPT API for chat and ElevenLabs API for text-to-speech and Vadoo API for  text-to-video. Alone with website services like Streamlit !

## Challenges we ran into

We spend most of our time to setup text-to-speech and text-to-video. Since both field is relatively new, not lots great APIs we can use. We tried more than 20 different companies, send out dozen of emails requires for API. Especially for the Text-to-Video, Vadoo is our only option and its API still in very early stage, lots of API fields are not work as it should. We tried so many ways, even open a webpage then feed URL to Vadoo to let it generated video, still lack of use.

## Accomplishments that we're proud of

We be able to have agent give out pitches in less than 1 second. Users can adjust how long the pitch need to be. As well as voice of the pitch with super realistic tone!  All of our Hackathon friends can use this now to pitch their ideas! We proud of that we be able to find ways around to get to where we are right now.

## What we learned
For the website design, we had to quickly learn Streamlit to create a cohesive layout and deploy it on both GitHub and local servers. 
We learned so much from building this little AI tool, mostly learned from text-to-video side, we now have sense of how new this field is. We learned a lot from customer side, knowing what we really want those TTV platform to achieve, but only about 20% of platform we experienced can do what we want. But still in low quality. You can do so much things even today.

## What's next for Elevator Pitch Chatbot with Video and Human-like Speech

We need a better way to show user Video, and the API for TTV could be updated to other platform. Even we can build on top of a fine tone model, if there's enough resource. Eventually I hope our tool can be open source and used for more purposes.

## Run it locally

```sh
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run Chatbot.py
```