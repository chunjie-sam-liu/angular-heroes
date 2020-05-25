import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { Post } from './models/Post';
import { Observable, of } from 'rxjs';
import { catchError, map, tap } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class FlaskapiService {

  constructor(
    private httpClient: HttpClient
  ) { }

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };

  public server = 'http://localhost:5000/api/';
  public getPosts(): Observable<Post[]> {
    return this.httpClient.get<Post[]>(this.server + 'posts')
    .pipe(
      catchError(this.handleError<Post[]>('getPosts', []))
    );
  }
  public getPost(postId: string) {
    return this.httpClient.get<Post>(this.server + `post/${postId}`);
  }
  public addPost(postObj: Post, image: any) {
    const {title, content} = postObj;
    const formData: FormData = new FormData();

    formData.append('title', title);
    formData.append('content', content);
    formData.append('cover', image[0], image.filename);

    return this.httpClient.post<Post>(this.server + 'addpost', formData);
  }

  public getImage(imageName: string): string {
    // get Image from backend
    return this.server + `image/${imageName}`;
  }

  private handleError<T>(operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {

      // TODO: send the error to remote logging infrastructure
      console.error(error); // log to console instead

      // TODO: better job of transforming error for user consumption
      // this.log(`${operation} failed: ${error.message}`);

      // Let the app keep running by returning an empty result.
      return of(result as T);
    };
  }

}
