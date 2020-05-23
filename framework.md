## Framework
1. Basic building blocks are **NgModules** which provide a compilation context for components. NgModules collect related code into function sets;
2. An Angular app is defined by a set of NgModules.
3. An app always has at least a root module that enables bootstrapping, and typically has many more feature modules.
4. Components define views.
5. Components use services, which provide specific functionality not directly related to views. Service providers can be injected into components as dependencies, making your code modular, reusable and efficient.
6. Both components and services are simply classes with decorators that mark their type and provide metadata tells Angular how to use them.

## Module
1. An NgModule declares a compilation context for a set of components that is dedicated to an application domain, a workflow, or a closely related set of capabilities.
2. An NgModule can associate its components with related code, such as services to form functional units.
3. Every Angular app has a root module, named AppModudle, which provides the bootstrap mechanism that launches the application.
4. An app typically contains many functional modules.

## Template, directives and data binding
1. Event binding lets your app respond to user input in the target environment by updating your application data.
2. Property binding lets you interpolate values that are computed from your application data into the HTML.

## Services and dependency injection
1. For data or logic that isn't associated with a specific view, and that you want to share across components, you create a service class. A service class definition is immediately preceded by the @Injectable() decorator. The decorator provides the metadata that allows other providers to be Injected as dependencies into your class.

## Routing

1. The router maps URL-like paths to views instead of pages.
2. Lazy-load.




