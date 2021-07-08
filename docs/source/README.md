# Parking Montpellier

<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Issues][issues-shield]][issues-url]
[![pull-request][pull-request-shield]][pull-request-url]
[![LS][LS-shield]][LS-url]
[![LinkedIn][linkedin-shield1]][linkedin-url1]
[![LinkedIn][linkedin-shield2]][linkedin-url2]
[![Python application](https://github.com/Mancid/parking_mtp/actions/workflows/python_app.yml/badge.svg?branch=main)](https://github.com/Mancid/parking_mtp/actions/workflows/python_app.yml)





<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/Mancid/">
    <img src="_images/mancid.png" alt="Logo" width="432" height="432">
  </a>
  <h2 align="center">MANCID Project present</h3>
<br />
</p>
<p align="center">
  <a href="https://github.com/Mancid/parking_mtp">
    <img src="_images/parking-3.png" alt="Logo" width="240" height="240">
  </a>
    <a href="https://github.com/Mancid/parking_mtp">
    <img src="_images/mtp.jpg" alt="Logo" width="319" height="240">
  </a>
  <h3 align="center">PARKING MONTPELLIER</h3>

  <p align="center">
    Visualisation en temps réel des places disponibles des parkings souterrains de Montpellier
    <br />
    <a href="https://mancid.github.io/parking_mtp/"><strong>Explore the docs »</strong></a>
    <br />
    <br />
  </p>
</p>


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <!-- <li><a href="#usage">Usage</a></li> -->
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

Ce projet permet de récupérer sur le site [OPENDATA de Montpellier Méditerranée Métropole](https://data.montpellier3m.fr/dataset/disponibilite-des-places-dans-les-parkings-de-montpellier-mediterranee-metropole) les données en format .xml sur la disponibilité des places de parking

### Built With

Voici les frameworks utilisés pour ce projet :

<a href="https://www.python.org/">&emsp;
<img src="_images/python.png" alt="image" width="65" height="65">
</a>
<a href="https://flask.palletsprojects.com/en/1.1.x/">&emsp; &emsp;
<img src="_images/flask.png" alt="Logo" width="87" height="65">
</a>
<a href="https://www.mongodb.com/fr-fr">&emsp; &emsp;
<img src="_images/mongodb.png" alt="Logo" width="63" height="65">
</a>
<a href="https://www.docker.com/">&emsp; &emsp;
<img src="_images/docker.png" alt="Logo" width="76" height="65">
</a>
<a href="https://www.heroku.com">&emsp; &emsp;
<img src="_images/heroku.png" alt="Logo" width="195" height="65">
</a>




<!-- GETTING STARTED -->
## Getting Started

Pour mettre en place une copie locale et la faire fonctionner, suivez les étapes simples de ce projet.

### Prerequisites

Liste des logiciels et librairies nécessaires et leurs installtions :  
* Python + pip + virtualenv

  ```sh
  $ sudo apt-get install python3 python3-pip python3-virtualenv
  ```

### Installation


1. Clone the repo
   ```sh
   $ git clone https://github.com/Mancid/parking_mtp.git
   ```
2. Se placer dans le dossier du repo
   ```sh
   $ cd parking_mtp
   ```
3. Install Python packages
   ```sh
   $ python -m virtualenv .venv
   ```
4. Activer l'environnement virtuel
   ```sh
   $ source ./.venv/bin/activate
   ```
5. Install Python packages
   ```sh
   $ pip install -r requirements.txt
   ```
6. Exécuter le `Script.sh` pour créer les environnement et démarrer l'API Flask
   ```JS
   $ ./Script.sh
   ```



<!-- USAGE EXAMPLES -->
<!-- ## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_ -->



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/Mancid/parking_mtp/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Contributors - [@DamienPlantin](https://github.com/DamienPlantin) - [@Nico34000](https://github.com/Nico34000)

Project Link: [https://github.com/Mancid/parking_mtp](https://github.com/Mancid/parking_mtp)



<!-- ACKNOWLEDGEMENTS -->
<!-- ## Acknowledgements
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Img Shields](https://shields.io)
* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Pages](https://pages.github.com)
* [Animate.css](https://daneden.github.io/animate.css)
* [Loaders.css](https://connoratherton.com/loaders)
* [Slick Carousel](https://kenwheeler.github.io/slick)
* [Smooth Scroll](https://github.com/cferdinandi/smooth-scroll)
* [Sticky Kit](http://leafo.net/sticky-kit)
* [JVectorMap](http://jvectormap.com)
* [Font Awesome](https://fontawesome.com) -->





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Mancid/parking_mtp
[contributors-url]: https://github.com/Mancid/parking_mtp/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Mancid/parking_mtp
[forks-url]: https://github.com/Mancid/parking_mtp/network/members
[issues-shield]: https://img.shields.io/github/issues/Mancid/parking_mtp
[issues-url]: https://github.com/Mancid/parking_mtp/issues
[pull-request-shield]: https://img.shields.io/github/issues-pr/Mancid/parking_mtp
[pull-request-url]: https://github.com/Mancid/parking_mtp/pulls
[linkedin-shield1]: https://img.shields.io/badge/-LinkedIn_Damien_Plantin-black&logo=linkedin&colorB=555
[linkedin-shield2]: https://img.shields.io/badge/-LinkedIn_Nicolas_Prodhomme-black&logo=linkedin&colorB=555
[linkedin-url1]: https://www.linkedin.com/in/damienplantin/
[linkedin-url2]: https://www.linkedin.com/in/nicolas-prodhomme-5578aa201/
[product-screenshot]: images/screenshot.png
<!-- [CI-shield]:https://img.shields.io/travis/com/mancid/parking_mtp?style=for-the-badge
[CI-url]:https://github.com/Mancid/parking_mtp/actions -->
[LS-shield]:https://img.shields.io/github/last-commit/Mancid/parking_mtp
[LS-url]:https://github.com/Mancid/parking_mtp/commits/main