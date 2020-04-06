import { Component, OnInit, Output,EventEmitter } from '@angular/core';
import { Recipe } from '../recipes.models'


@Component({
  selector: 'app-recipes-list',
  templateUrl: './recipes-list.component.html',
  styleUrls: ['./recipes-list.component.css']
})
export class RecipesListComponent implements OnInit {
  @Output() recipeWasSelected = new EventEmitter<Recipe>();

  recipes:Recipe[]=[
    new Recipe('A test Recipe','this is a simply test',
    'https://thumbs.dreamstime.com/b/assorted-indian-food-set-tray-tanduri-chicken-naan-bread-yoghurt-traditional-curry-roti-dinner-129820124.jpg'),

    new Recipe('A test Other Recipe','this is a simply test',
    'https://i.ytimg.com/vi/N9vNEUPXT1M/hqdefault.jpg')
  ]

  constructor() { }

  ngOnInit(): void {
  }

  onRecipeSelected(recipe:Recipe){
  this.recipeWasSelected.emit(recipe)
  }
}
