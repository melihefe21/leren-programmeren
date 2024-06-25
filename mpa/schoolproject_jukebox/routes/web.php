<?php
use App\Http\Controllers\PlaylistController;
use App\Http\Controllers\ViewsController;
use App\Http\Controllers\Welcome;
use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('products/index');
});
Route::get("/hello", [welcome::class, "hello"]);

Route::get("/hello", [ViewsController::class, "hello"])->name('hello');


Route::get('views', function () {
    return view('layout/master');
});

Route::get("/views", [ViewsController::class, "index"]);

Route::get("/playlist/all", [PlaylistController::class,"index"]);
Route::get("/playlist/view/{playlist}", [PlaylistController::class,"show"]);
Route::post("/playlist/addsong/{playlist}", [PlaylistController::class, "AddSongtoPlaylist"]);