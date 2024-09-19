@extends("layouts.master")

@section("content")

    <h1>Hier is 1 lijst met alle liedjes....{{Auth::user()->name}}</h1>
    <ul>
        @foreach ($songs as $song)
            <li>{{$song->name}} - {{$song->genre->name}}</li>
        @endforeach
    </ul>
@endsection