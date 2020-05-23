import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';


import { PostRoutingModule } from './post-routing.module';
import { PostComponent } from './post.component';



@NgModule({
  imports: [
    CommonModule,
    PostRoutingModule
  ],
  declarations: [PostComponent]
})
export class PostModule { }
