import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { ReactiveFormsModule } from '@angular/forms';


import { PostRoutingModule } from './post-routing.module';
import { PostComponent } from './post.component';



@NgModule({
  imports: [
    CommonModule,
    ReactiveFormsModule,
    PostRoutingModule
  ],
  declarations: [PostComponent]
})
export class PostModule { }
