// attribution des tetes de chat
const cat1 = './Public/img/tete_chat/cat_1.png',
	cat2 = './Public/img/tete_chat/cat_2.png',
	cat3 = './Public/img/tete_chat/cat_3.png',
	cat4 = './Public/img/tete_chat/cat_4.png',
	cat5 = './Public/img/tete_chat/cat_5.png',
	cat6 = './Public/img/tete_chat/cat_6.png',
	cat7 = './Public/img/tete_chat/cat_7.png',
	cat8 = './Public/img/tete_chat/cat_8.png',
	cat9 = './Public/img/tete_chat/cat_9.png',
	cat10 = './Public/img/tete_chat/cat_10.png'

let array = [cat1, cat2, cat3, cat4, cat5, cat6, cat7, cat8, cat9, cat10]
// mélange des têtes de chats
function shuffle(array) {
	const newArray = array
	const length = newArray.length

	for (let start = 0; start < length; start++) {
		const randomPosition = Math.floor((newArray.length - start) * Math.random())
		const randomItem = newArray.splice(randomPosition, 1)
		newArray.push(...randomItem)
	}
	return newArray
}

// Génération d'un nombre random
function randomNumber(min, max) {
	return Math.floor(Math.random() * (max - min) + min)
}

//Attribution aléatoire des têtes de chat

function attributeCat(array) {
	const shuffledArray = shuffle(array)
	let catContainers = document.querySelectorAll('.cat')

	for (let i = 0; i < catContainers.length; i++) {
		catContainers[i].src = shuffledArray[i]
	}
	//calcul d'un nombre aléatoire pour déterminer la position (dans le tableau)de la tête de chat a trouver
	const randomCat = randomNumber(0, catContainers.length)

	const startGame = document.getElementById('start_game')
	const oldCat = document.getElementById('oldCat')

	// si on clique pour initier le jeu
	startGame.addEventListener('click', (e) => {
		searchedCat(shuffledArray, randomCat, catContainers)
	})

	//si le jeu est relancé
	if (oldCat) {
		searchedCat(shuffledArray, randomCat, catContainers)
	}
}

//Affichage de la tête de chat à chercher
function searchedCat(shuffledArray, randomCat, catContainers) {
	const searchCat = shuffledArray[randomCat]
	//création de l'élément et attribution de l'image a chercher
	const findCat = document.createElement('IMG')
	findCat.setAttribute('id', 'newCat')
	findCat.src = searchCat

	const rep = document.getElementById('reponse_1-p')

	const oldP = document.getElementById('oldCat')
	//si le jeu est joué pour la première foi
	if (rep) {
		document.getElementById('reponse_1-parent').replaceChild(findCat, rep)
	}
	//si le jeu est rejoué
	else if (oldP) {
		document.getElementById('reponse_1-parent').replaceChild(findCat, oldP)
	}

	findTheCat(catContainers, searchCat)
}

//Trouver le bon chat
function findTheCat(catContainers, searchCat) {
	//ecoute pour toutes les boites à chat
	catContainers.forEach((catContainer) => {
		catContainer.addEventListener('click', (e) => {
			const catSrc = e.currentTarget.getAttribute('src')
			const gameResult = document.getElementById('game_result')
			//si l'image est la même que celle à trouver
			if (catSrc === searchCat) {
				//affichage de la victoire et possibilité de rejouer
				
				gameResult.innerText = 'Vous avez gagné'
				gameResult.innerHTML = `
				<div class="result__container"> <div class="result__content">
				<p>Félicitations Vous avez gagné</p>
				<p>Voulez-vous <span id="new__game">rejouer?</span></p>
				<div id="close">X</div>
				</div></div>`
				gameResult.style.zIndex = '10'
				gameResult.style.transform = 'translateY(-420px)'
				gameResult.style.transition = ' all 0.5s'

				newGame(array, gameResult)
			}
		})
	})
}

//relancer le jeu
function newGame(array, gameResult) {
	const newGameSpan = document.getElementById('new__game')
	const endGame=document.getElementById('close')
	const oldCat = document.getElementById('newCat')

	//ne pas relancer le jeu et revenir à la configuration du début
	endGame.addEventListener('click', (e) => {
		//clean gameResult
		gameResult.style.zIndex = '-10'
		gameResult.innerText = ''
		gameResult.innerHTML = ``

		const rejouer= document.createElement('p')
		rejouer.innerText='Oui je veux jouer' 
		rejouer.setAttribute('id', 'reponse_1-p')
		document.getElementById('reponse_1-parent').replaceChild(rejouer, oldCat)
		
		attributeCat(array)

	})

	//rejouer 
	newGameSpan.addEventListener('click', (e) => {

		//modification de l'id de l'ancienne photo à trouver pour pouvoir la remplacer
		oldCat.setAttribute('id', 'oldCat')

		attributeCat(array)

		//clean gameResult
		gameResult.style.zIndex = '-10'
		gameResult.innerText = ''
		gameResult.innerHTML = ``
	})
}


attributeCat(array)
