
@extends('layouts.master')

@section('content')
    <div class="container">
        <h1 class="text-center my-4">List of Songs</h1>

        <div class="row justify-content-center">
            <div class="col-md-8">
                <div class="card">
                    <div class="card-header bg-primary text-white text-center">Songs</div>

                    <div class="card-body">
                        @if(count($songs))
                            <ul class="list-group">
                                @foreach ($songs as $song)
                                    <li class="list-group-item d-flex justify-content-between align-items-center">
                                        {{ $song->title }}
                                        <span class="badge bg-secondary">{{ $song->artist }}</span>
                                    </li>
                                @endforeach
                            </ul>
                        @else
                            <p class="text-center">No songs available.</p>
                        @endif
                    </div>
                </div>
            </div>
        </div>
    </div>

    @push('scripts')
        <script>
            console.log("Songs list loaded successfully");
        </script>
    @endpush
@endsection
