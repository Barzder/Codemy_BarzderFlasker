function load() {
  // The buttons used to toggle the darkmode setting
  const themeButtons = document.querySelectorAll("#themebtn");

  // ID to be used for the buttons with "btn-outline-color" attribute
  const outlineButtonID = "outlineButton";

  // Scan all buttons to automatically assign the ID to all outline buttons
  const possibleOutlineButtons = document.querySelectorAll(".btn");
  validateOutlineButtons();

  // Gather all outline buttons in an array
  const outlineButtons = document.querySelectorAll("#"+outlineButtonID);

  // All colors for buttons
  const buttonColors = ['btn-primary','btn-secondary','btn-success','btn-danger','btn-warning','btn-info','btn-light','btn-dark'];

  // Gets the stored theme when switching pages
  function getStoredTheme(){
    return sessionStorage.getItem('theme');
  };
  
  // Stores the selected theme
  function setStoredTheme(theme){
    sessionStorage.setItem('theme', theme);
  };

  // Selects a stored theme or the preferred system theme 
  function getPreferredTheme(){
    const storedTheme = getStoredTheme();
    if (storedTheme) {
      return storedTheme;
    }
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  };

  // Changes the theme of the html element and changes the values of the toggle button
  function setTheme(theme){
    document.documentElement.setAttribute('data-bs-theme', theme);
    toggleButtonsChange(theme);
    outlineButtonsChange(theme);
  };

  // Initially sets the preferred system theme
  setTheme(getPreferredTheme());

  // Set the buttons to toggle the theme
  function toggleButtonsChange(theme){
    if (theme == "dark"){
      themeButtons.forEach(themeButton => {
        themeButton.setAttribute('data-bs-theme-value','light');
        themeButton.setAttribute('class','btn btn-sm btn-light');
        themeButton.querySelector('span').innerHTML = "light_mode";
      });
    }else{
      themeButtons.forEach(themeButton => {
        themeButton.setAttribute('data-bs-theme-value','dark');
        themeButton.setAttribute('class','btn btn-sm btn-dark');
        themeButton.querySelector('span').innerHTML = "dark_mode";
      });
    };
  };

  // Add the id to all buttons with "btn-outline-color" in the class
  function validateOutlineButtons(){
    possibleOutlineButtons.forEach(possibleOutlineButton => {
      const origClass = possibleOutlineButton.getAttribute('class');
      const splitClass = origClass.split(" ");
      splitClass.forEach(splitClassString => {
        const splitClassSnippet = splitClassString.split("-");
        splitClassSnippet.forEach(snippet => {
          if(snippet == "outline"){
            possibleOutlineButton.setAttribute('id',outlineButtonID);
          };
        });
      });
    });
  };

  // Set the bottons with outline buttons
  function outlineButtonsChange(theme){
    outlineButtons.forEach(outlineButton => {
      if(theme=="light"){
        const origClass = outlineButton.getAttribute('class');
        const modifiedClass = origClass.replace('outline-','');
        outlineButton.setAttribute('class', modifiedClass);
        outlineButton.setAttribute('class', modifiedClass);
      }else{
        const origClass = outlineButton.getAttribute('class');
        const splitClass = origClass.split(" ");
        splitClass.forEach(snippet => {
          if(buttonColors.includes(snippet)){
            const subSnippet = snippet.split('-');
            const newSnippet = subSnippet[0] + "-outline-" + subSnippet[1];
            const modifiedClass = origClass.replace(snippet,newSnippet);
            outlineButton.setAttribute('class', modifiedClass);
          }
        })
      }
    })
  }

  // Listen for changes in the OS settings
  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => {
    setTheme(window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
  });

  // Toggles the "dark-mode" on click
  themeButtons.forEach(themeButton => {
    themeButton.addEventListener("click", () => {
      const selectedTheme = themeButton.getAttribute('data-bs-theme-value');
      setTheme(selectedTheme);
      setStoredTheme(selectedTheme);
    });    
  });
};

window.addEventListener("DOMContentLoaded", load);
