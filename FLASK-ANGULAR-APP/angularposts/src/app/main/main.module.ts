import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';


import { MainRoutingModule } from './main-routing.module';
import { MainComponent } from './main.component';
import { AboutComponent } from './about/about.component';



@NgModule({
  imports: [
    CommonModule,
    MainRoutingModule
  ],
  declarations: [MainComponent, AboutComponent]
})
export class MainModule { }
