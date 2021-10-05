# CS350-Project-1
### LMAO Rater - Cards Against Humanity Edition
If you have any questions about the repo don't hesitate to reach out to me (John Minney) either on discord or in person. I'll help out however I can. Thanks!
***
### Helpful Links
* [Wireframes](https://drive.google.com/file/d/1AEX5SSGb8SkRphjMRcTisz7CaAjFmmYf/view?usp=sharing)
* [Trello Board](https://trello.com/invite/b/sG8NbTUa/ff1a6878bca18a700b2939722b832863/cs350-project-1-cards-against-humanity-lmao-rater)
* [Bootstrap](https://getbootstrap.com/)
* [Google Docs](https://docs.google.com/document/d/1h5SaQgaS8cBbChJ9sOJOn-tKTe_8QvTDyvLXEAc75DU/edit)
* [Branches Info](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches)
* [Super Awesome and Amazing Git Branch/PR Tutorial](https://youtu.be/0urqEJmf73s)
***
### Creating a Local Dev Enviroment
To create your own local dev enviroment follow the steps below.
> 1. Clone the repo to your local machine
> 2. Move your way to the project directory
> 3. Souce your virtual env (if you are using one)
> 4. Run the following commands
> * `python manage.py makemigrations`
> * `python manage.py migrate`   
> 5. Run your local server with `python manage.py runserver`

These steps will create a local version of the project and load your local dev database with dummy data. This data <strong>will</strong> with new data by the backend team.

<strong><em>Keey in Mind! Any Code you wite concerning the cards might need to change depending on the backend team's design decisions.</em></strong>

***
### Pushing to the Repo
Due to merge conflicts we will have a seperate branch for each team of developers or task. We can then use these branches to push code without causing merge conflicts between the teams/tasks. Below are the instructions to change branches.

Make Sure to Checkout Jacob's Tutorial. It is amazing [Video Link](https://youtu.be/0urqEJmf73s)

To create a branch you can either follow the steps below or ask me (John Minney) and I can get it set up for you.
> * While looking at the Github page for the project look for a dropdown menu that will most likely say "main"
> * Click on this dropdown and make sure you are on the main branch
> * Enter the name of your new branch in the text box
> * Once you enter the name there will be a section that says "Create branch: branch_name from 'main'
> * Click that and it will create the new branch
> * Once you have created the new branch pull on your local machine and you will be able to checkout the new branch

For the following steps replace *branch_name* with your teams working branch.
If you are using git bash (command line) follow these steps to switch branches.
> If you are using a UI follow their documentation or tutorial videos to switch branches
* Find your way to the local version of the project
* Type the command `git branch -a`
* If you don't see your branch listed run `git pull`
* If you can locate your branch use the command `git checkout branch_name`
* You are now working on your team's branch. Push code like you would normally

**Important!!**
The first time you push to the branch use the command `git push -u origin branch_name`

When you are done working on your branch create a Pull Request for the code to be reviewed. This will allow me to ensure that any new code won't cause a merge conflict on the production version.
***
