import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { ReactiveFormsModule } from '@angular/forms';

import { AddpostRoutingModule } from './addpost-routing.module';
import { AddpostComponent } from './addpost.component';



@NgModule({
  imports: [
    CommonModule,
    ReactiveFormsModule,
    AddpostRoutingModule
  ],
  declarations: [AddpostComponent]
})
export class AddpostModule { }
