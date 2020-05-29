import { Component, OnInit } from '@angular/core';
import { FlaskapiService } from '../flaskapi.service';
import { ActivatedRoute, Router } from '@angular/router';
import { Subscription } from 'rxjs';
import { Post } from '../models/Post';
import { FormGroup, FormControl, Validators } from '@angular/forms';



@Component({
  selector: 'app-post',
  templateUrl: './post.component.html',
  styleUrls: ['./post.component.css']
})
export class PostComponent implements OnInit {

  constructor(
    private flaskApiService: FlaskapiService,
    private route: ActivatedRoute,
    private router: Router
  ) { }

  public currentID: any = this.route.snapshot.paramMap.get('id');
  public postSubscription: Subscription;
  public editSubscription: Subscription;
  public post: Post;
  public editMode = false;
  public image: any;
  public busy: boolean;
  public imageURL: string;

  public editForm = new FormGroup({
    title: new FormControl('', Validators.required),
    content: new FormControl('', Validators.required),
    // oldcover: new FormControl('', Validators.required),
    // id: new FormControl('', Validators.required),
    cover: new FormControl('', Validators.required)
  });

  public getPostById() {
    this.postSubscription = this.flaskApiService.getPost(this.currentID)
      .subscribe(res => {
        // tslint:disable-next-line: no-string-literal
        this.post = res['data'];
        console.log(this.post);
        this.editForm.setValue({
          title: this.post.title,
          content: this.post.content,
          oldcover: this.post.cover,
          covername: this.post.covername
        });
      });
  }
  public getImage(imageName: string): string {
    this.imageURL = this.flaskApiService.getImage(imageName);
    return this.imageURL;
  }
  public enableEdit(): void {
    this.editMode = this.editMode ? false : true ;
  }
  public deletePost(title: string): void {

  }
  public editPost(post: Post): void {

  }

  public handleInput($event: Event): void {

  }

  ngOnInit(): void {
    this.getPostById();
  }

}
